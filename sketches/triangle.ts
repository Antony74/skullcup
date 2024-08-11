import p5 from 'p5';
import { Tuple2, Tuple3, Tuple4, tupleMap } from '../src/tuples';

export type Triangle = Tuple3<{ vec: p5.Vector }>;

export const drawTriangle = (
    p: p5,
    triangle: Triangle,
    fillColor: Tuple4<number>,
    strokeColor: Tuple4<number> = [0, 0, 0, 0],
) => {
    p.push();
    p.stroke(...strokeColor);
    p.fill(...fillColor);
    p.beginShape();
    triangle.forEach((vertex) => p.vertex(vertex.vec.x, vertex.vec.y));
    p.endShape('close');
    p.pop();
};

export const triangleAsTuples = (
    triangle: Triangle,
): Tuple3<Tuple2<number>> => {
    return tupleMap<{ vec: p5.Vector }, Tuple2<number>, 3>(
        triangle,
        (vertex) => [vertex.vec.x, vertex.vec.y],
    );
};
