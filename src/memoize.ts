export const memoize = <ParamsType extends Array<any>, ReturnType>(
    fn: (...params: ParamsType) => ReturnType,
) => {
    const cache: Record<string, ReturnType> = {};
    return (...params: ParamsType) => {
        const key = JSON.stringify(params);
        return cache[key] ? cache[key] : (cache[key] = fn(...params));
    };
};

export const memoizeBounded = <ParamsType extends Array<any>, ReturnType>(
    fn: (...params: ParamsType) => ReturnType,
    maxSize: number,
) => {
    const cache: Record<string, ReturnType> = {};
    return (...params: ParamsType) => {
        const key = JSON.stringify(params);
        const result = cache[key] ? cache[key] : (cache[key] = fn(...params));

        const keys = Object.keys(cache);
        if (keys.length > maxSize) {
            delete cache[keys[0]];
        }

        return result;
    };
};
