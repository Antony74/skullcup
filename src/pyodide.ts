import { loadPyodide } from 'pyodide';
import { memoize } from './memoize';
import 'pyodide/pyodide.asm.js';

export const getPyodide = memoize(async () => {
    const pyodide = await loadPyodide();

    await pyodide.loadPackage('numpy');
    await pyodide.runPythonAsync(`import numpy as np`);

    return pyodide;
});
