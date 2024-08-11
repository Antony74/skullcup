const memoizeExposed = <ParamsType extends Array<any>, ReturnType>(
    fn: (...params: ParamsType) => ReturnType | Promise<ReturnType>,
) => {
    const cache: Record<string, ReturnType | Promise<ReturnType>> = {};

    return {
        fn: (...params: ParamsType) => {
            const key = JSON.stringify(params);
            if (cache[key]!== undefined) {
                return cache[key];
            } else {
                const result = fn(...params);
                if (result instanceof Promise) {
                    result.then((value) => {
                        cache[key] = value;
                    });
                }
                cache[key] = result;
                return result;
            }
        },
        getCache: () => {
            return cache;
        },
    };
};

export const memoize = <ParamsType extends Array<any>, ReturnType>(
    fn: (...params: ParamsType) => ReturnType | Promise<ReturnType>,
) => memoizeExposed(fn).fn;

export const memoizeBounded = <ParamsType extends Array<any>, ReturnType>(
    fn: (...params: ParamsType) => ReturnType | Promise<ReturnType>,
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
