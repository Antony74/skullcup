import { Matrix, NumberTuple } from './tuples';
import { solve } from './linalg';

const main = async () => {
    const matrix: Matrix<3, 3> = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
    ];

    const vector: NumberTuple<3> = [0.25, 0.25, 1];

    const result = await solve<3, 3>(matrix, vector);
    console.log(result);
};

main();
