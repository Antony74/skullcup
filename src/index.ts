import { Matrix, NumberTuple } from './tuples';
import { solve } from './linalg';
import { pointInSimplex } from './simplex';

const main = async () => {
    const matrix: Matrix<3, 3> = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
    ];

    const vector: NumberTuple<3> = [0.25, 0.25, 1];

    const result = await solve<3, 3>(matrix, vector);
    console.log(result);

    const vertices: Matrix<2, 3> = [
        [0, 0],
        [1, 0],
        [1, 1],
    ];

    const pointInside: NumberTuple<2> = [0.25, 0.25];
    const pointOutside: NumberTuple<2> = [1, 1];

    const result1 = await pointInSimplex(vertices, pointInside);

    console.log(result1); // true

    const result2 = await pointInSimplex(vertices, pointOutside);

    console.log(result2); // false
};

main();
