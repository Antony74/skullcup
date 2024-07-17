// Recursive definitions of a Tuple break as soon as I try to define a matrix that way
// so without overriding the type checking or adding more Tuple types we are limited to
// the number of dimensions defined here.  Much as I have tried to generalize everything,
// I can't see myself ever using more than three dimensions in earnest or four playfully,
// anyway.

export type TupleSize = 2 | 3 | 4 | 5;
export type TuplePlusOneSize = 1| 2 | 3 | 4 | 5 | 6;

export type Tuple2<T> = [T, T];
export type Tuple3<T> = [T, T, T];
export type Tuple4<T> = [T, T, T, T];
export type Tuple5<T> = [T, T, T, T, T];
export type Tuple6<T> = [T, T, T, T, T, T];

export type Tuple<T, N extends TupleSize | TuplePlusOneSize> = N extends 2
    ? Tuple2<T>
    : N extends 3
    ? Tuple3<T>
    : N extends 4
    ? Tuple4<T>
    : N extends 5
    ? Tuple5<T>
    : Tuple6<T>;

export type Vector<N extends TupleSize> = Tuple<number, N>;
export type VectorPlusOneSize<N extends TuplePlusOneSize> = Tuple<number, N>;

export type Matrix<N extends TupleSize, M extends TupleSize> = Tuple<
    Vector<N>,
    M
>;
