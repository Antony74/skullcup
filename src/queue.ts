export type Queue<T> = {
    pushBack: (t: T) => void;
    popFront: () => T;
    front: () => T;
    size: () => number;
    empty: () => boolean;
};

type QueueItem<T> = {
    t: T;
    prev: QueueItem<T> | undefined;
};

export const createEmptyQueue = <T>(): Queue<T> => {
    let back: QueueItem<T> | undefined = undefined;
    let front: QueueItem<T> | undefined = undefined;
    let size = 0;

    const queue: Queue<T> = {
        pushBack: (t: T) => {
            const queueItem = { t, prev: undefined };
            if (back !== undefined) {
                back.prev = queueItem;
            }
            back = queueItem;
            if (front === undefined) {
                front = queueItem;
            }
            ++size;
        },
        popFront: (): T => {
            const result = front;
            if (result === undefined) {
                throw new Error(`popFront called on empty queue`);
            } else {
                front = result.prev;
                if (front === undefined) {
                    back = undefined;
                }
                --size;
                return result.t;
            }
        },
        front: () => {
            if (front === undefined) {
                throw new Error(`front called on empty queue`);
            } else {
                return front.t;
            }
        },
        size: () => size,
        empty: () => size === 0,
    };

    return queue;
};
