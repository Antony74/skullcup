import { loadPyodide } from 'pyodide';

// Cause packages to be cached

const main = async () => {
    const pyodide = await loadPyodide();
    await pyodide.loadPackage('numpy');
    await pyodide.loadPackage('scipy');
};

main();
