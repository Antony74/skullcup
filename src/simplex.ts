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
import { Matrix, NumberTuple } from './tuples';
import { solve } from './linalg';

export const pointInSimplex = (vertices: number[][], point: number[]) => {
    console.log(vertices[0]);

    const matrix = [
        ...point.map((_value, index) => {
            return vertices.map((value) => value[index]);
        }),
        [...point.map(() => 1), 1],
    ];

    const vector = [...point, 1];

    console.log(JSON.stringify({ matrix, vector }, null, 4));

    return solve<2, 3>(matrix as any, vector as any);
};
