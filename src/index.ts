import { loadPyodide } from 'pyodide';

const main = async () => {
    const pyodide = await loadPyodide();
    pyodide.runPythonAsync(`print('py says hi')`);
};

main();
