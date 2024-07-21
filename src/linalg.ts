import { getPyodide } from './pyodide';
import { Matrix, Vector } from './tuples';

export const solve = async <N extends number, M extends number>(
    matrix: Matrix<N, M>,
    vector: Vector<M>,
): Promise<Vector<M>> => {
    const pyodide = await getPyodide();

    pyodide.globals.set('matrix', matrix);
    pyodide.globals.set('vector', vector);

    const result = await pyodide.runPythonAsync(
        `np.linalg.solve(matrix, vector)`,
    );

    return result.toJs();
};
