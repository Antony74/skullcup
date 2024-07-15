import { loadPyodide } from 'pyodide';

type _TupleOf<T, N extends number, R extends T[]> = R['length'] extends N
    ? R
    : _TupleOf<T, N, [T, ...R]>;

type Tuple<T, N extends number> = _TupleOf<T, N, []>;

type NumberTuple<N extends number> = Tuple<number, N>;

type Matrix<N extends number, M extends number> = Tuple<NumberTuple<N>, M>;

const linalg = async <N extends number, M extends number>(
    matrix: Matrix<N, M>,
    vector: NumberTuple<N>
): Promise<NumberTuple<N>> => {
    const pyodide = await loadPyodide();

    await pyodide.loadPackage('numpy');
    await pyodide.runPythonAsync(`import numpy as np`);

    pyodide.globals.set('matrix', matrix);
    pyodide.globals.set('vector', vector);

    const result = await pyodide.runPythonAsync(
        `np.linalg.solve(matrix, vector)`
    );
    return result.toJs();
};

const main = async () => {
    const matrix: Matrix<3, 3> = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
    ];

    const vector: NumberTuple<3> = [0.25, 0.25, 1];

    const result = await linalg<3, 3>(matrix, vector);
    console.log(result);
};

main();
