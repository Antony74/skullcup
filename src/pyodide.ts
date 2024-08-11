import { loadPyodide } from 'pyodide';
import { memoize } from './memoize';
import 'pyodide/pyodide.asm.js';
import { createEmptyQueue, Queue } from './queue';

export enum PyodideInstanceNames {
    sole,
}

export type PyodideJob = {
    globals: Record<string, any>;
    code: string;
    resolve: (result: any) => void;
    cancelled?: boolean;
};

type PyodideInstance = {
    pushJob: (job: PyodideJob) => void;
    cancelAllJobs: () => void;
};

export const getPyodide = memoize(
    async (_instanceName: PyodideInstanceNames): Promise<PyodideInstance> => {
        const pyodide = await loadPyodide();

        await pyodide.loadPackage('numpy');
        await pyodide.runPythonAsync(`import numpy as np`);

        let running = false;
        const queue: Queue<PyodideJob> = createEmptyQueue();

        const runJobs = async () => {
            running = true;

            while (queue.size()) {
                const job = queue.popFront();

                if (job.cancelled) {
                    continue;
                }

                Object.entries(job.globals).forEach(([name, value]) =>
                    pyodide.globals.set(name, value),
                );

                const result = await pyodide.runPythonAsync(job.code);
                job.resolve(result);
            }

            running = false;
        };

        return {
            pushJob: async (job: PyodideJob) => {
                queue.pushBack(job);
                if (running == false) {
                    runJobs();
                }
            },

            cancelAllJobs: () => {},
        };
    },
);
