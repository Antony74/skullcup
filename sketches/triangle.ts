import p5 from 'p5';
import { Tuple3, Tuple4 } from '../src/tuples';

export type Triangle = Tuple3<p5.Vector>;

export const drawTriangle = (
    p: p5,
    triangle: Triangle,
    fillColor: Tuple4<number>,
    strokeColor: Tuple4<number> = [0, 0, 0, 0]
) => {
    p.push();
    p.stroke(...strokeColor);
    p.fill(...fillColor);
    p.beginShape();
    triangle.forEach((vertex) => p.vertex(vertex.x, vertex.y));
    p.endShape('close');
    p.pop();
};
