// def is_point_in_simplex(vertices, point):
//     vertices = np.array(vertices)
//     point = np.array(point)
//     num_vertices = vertices.shape[0]
//     A = np.vstack((vertices.T, np.ones(num_vertices)))
//     b = np.append(point, 1)
//     try:
//         barycentric_coords = np.linalg.solve(A, b)
//     except:
//         return False
//     return np.all(barycentric_coords >= 0) and np.isclose(barycentric_coords.sum(), 1)

import { Add } from 'ts-arithmetic';
import { solve } from './linalg';
import {
    Vector,
    Matrix,
    matrixTranspose,
    tupleAppend,
    tupleMap,
} from './tuples';

export const pointInSimplex = async <N extends number, M extends number>(
    vertices: Matrix<N, M>,
    point: Vector<N>
) => {
    const matrix = tupleAppend(
        matrixTranspose(vertices),
        tupleMap(vertices, () => 1)
    );

    const vector: Vector<Add<N, 1>> = tupleAppend(point, 1);

    const barycentricCoords = await solve<M, Add<N, 1>>(matrix, vector);

    return (
        barycentricCoords.every((value) => value >= 0) &&
        barycentricCoords.reduce((acc, value) => acc + value, 0) === 1
    );
};
