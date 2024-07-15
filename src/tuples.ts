type _TupleOf<T, N extends number, R extends T[]> = R['length'] extends N
    ? R
    : _TupleOf<T, N, [T, ...R]>;

export type Tuple<T, N extends number> = _TupleOf<T, N, []>;

export type NumberTuple<N extends number> = Tuple<number, N>;

export type Matrix<N extends number, M extends number> = Tuple<NumberTuple<N>, M>;
