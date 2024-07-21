export const memoize = <ParamsType extends Array<any>, ReturnType>(
    fn: (...params: ParamsType) => ReturnType,
) => {
    const cache: Record<string, ReturnType> = {};
    return (...params: ParamsType) => {
        const key = JSON.stringify(params);
        return cache[key] ? cache[key] : (cache[key] = fn(...params));
    };
};
