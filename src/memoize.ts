const memoizeExposed = <ParamsType extends Array<any>, ReturnType>(
    fn: (...params: ParamsType) => ReturnType,
) => {
    const cache: Record<string, ReturnType> = {};

    return {
        fn: (...params: ParamsType) => {
            const key = JSON.stringify(params);
            return cache[key] ? cache[key] : (cache[key] = fn(...params));
        },
        getCache: (): Record<string, ReturnType> => {
            return cache;
        },
    };
};

export const memoize = <ParamsType extends Array<any>, ReturnType>(
    fn: (...params: ParamsType) => ReturnType,
) => memoizeExposed(fn).fn;

export const memoizeBounded = <ParamsType extends Array<any>, ReturnType>(
    fn: (...params: ParamsType) => ReturnType,
    maxSize: number,
) => {
    const base = memoizeExposed(fn);

    return (...params: ParamsType) => {
        const result = base.fn(...params);
        const cache = base.getCache();

        const keys = Object.keys(cache);
        if (keys.length > maxSize) {
            delete cache[keys[0]];
        }

        return result;
    };
};
