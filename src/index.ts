import { Matrix, Vector } from './tuples';
import { pointInSimplex } from './simplex';

const main = async () => {
    const vertices: Matrix<2, 3> = [
        [0, 0],
        [1, 0],
        [0, 1],
    ];

    const pointInside: Vector<2> = [0.25, 0.25];
    const pointOutside: Vector<2> = [1, 1];

    const result1 = await pointInSimplex<2>(vertices, pointInside);

    console.log(result1); // true

    const result2 = await pointInSimplex<2>(vertices, pointOutside);

    console.log(result2); // false
};

main();
