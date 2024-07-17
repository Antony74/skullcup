import { getPyodide } from './pyodide';
import { Matrix, Vector, TupleSize } from './tuples';

export const solve = async <N extends TupleSize, M extends TupleSize>(
    matrix: Matrix<N, M>,
    vector: Vector<N>
): Promise<Vector<N>> => {
    const pyodide = await getPyodide();

    pyodide.globals.set('matrix', matrix);
    pyodide.globals.set('vector', vector);

    const result = await pyodide.runPythonAsync(
        `np.linalg.solve(matrix, vector)`
    );

    return result.toJs();
};
