import { getPyodide, PyodideInstanceNames } from './pyodide';
import { Matrix, Vector } from './tuples';

export const solve = async <N extends number, M extends number>(
    matrix: Matrix<N, M>,
    vector: Vector<M>,
): Promise<Vector<M>> => {
    const pyodide = await getPyodide(PyodideInstanceNames.sole);

    return new Promise((resolve) =>
        pyodide.pushJob({
            globals: { matrix, vector },
            code: `np.linalg.solve(matrix, vector)`,
            resolve,
        }),
    );
};
