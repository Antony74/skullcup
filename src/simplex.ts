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

//import { Add } from 'ts-arithmetic';
import { solve } from './linalg';
import {
    Vector,
    TupleSize,
    Matrix,
    matrixTranspose,
    tupleAppend,
    tupleMap,
} from './tuples';

export const pointInSimplex = async <N extends TupleSize, M extends TupleSize>(
    vertices: Matrix<N, M>,
    point: Vector<N>
) => {
    const matrix: Matrix<M, N> = tupleAppend(
        matrixTranspose(vertices),
        tupleMap(vertices, () => 1)
    );

    const vector = tupleAppend<number, N, M>(point, 1);

    const barycentricCoords = await solve(matrix, vector);

    return (
        barycentricCoords.every((value) => value >= 0) &&
        barycentricCoords.reduce((acc, value) => acc + value, 0) === 1
    );
};
