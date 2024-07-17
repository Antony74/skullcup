// Recursive definitions of a Tuple break as soon as I try to define a matrix that way
// so without overriding the type checking or adding more Tuple types we are limited to
// the number of dimensions defined here.  Much as I have tried to generalize everything,
// I can't see myself ever using more than three dimensions in earnest or four playfully,
// anyway.

import { Add } from 'ts-arithmetic';

export type Tuple2<T> = [T, T];
export type Tuple3<T> = [T, T, T];
export type Tuple4<T> = [T, T, T, T];
export type Tuple5<T> = [T, T, T, T, T];
export type Tuple6<T> = [T, T, T, T, T, T];

export type Tuple<T, N extends number> = N extends 2
    ? Tuple2<T>
    : N extends 3
    ? Tuple3<T>
    : N extends 4
    ? Tuple4<T>
    : N extends 5
    ? Tuple5<T>
    : N extends 6
    ? Tuple6<T>
    : never;

export type Vector<N extends number> = Tuple<number, N>;

export type Matrix<N extends number, M extends number> = Tuple<
    Vector<N>,
    M
>;

export const tupleMap = <T1, T2, N extends number>(
    tuple: Tuple<T1, N>,
    fn: (t: T1, index: number) => T2
): Tuple<T2, N> => {
    const result = Array.from({ length: tuple.length }) as Tuple<T2, N>;
    for (let n = 0; n < tuple.length; ++n) {
        result[n] = fn(tuple[n], n);
    }
    return result;
};

export const tupleAppend = <T, N extends number>(
    tuple: Tuple<T, N>,
    t: T
) => {
    return [...tuple, t] as unknown as Tuple<T, Add<N, 1>>;
};

export const matrixTranspose = <N extends number, M extends number>(
    matrix: Matrix<N, M>
): Matrix<M, N> => {
    return tupleMap(matrix[0], (_value, m) => {
        return tupleMap(matrix, (_vector, n) => {
            return matrix[n][m];
        });
    });
};
