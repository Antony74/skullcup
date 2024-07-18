import p5 from 'p5';
import { Tuple2, Tuple3, Tuple4 } from '../src/tuples';

export type Triangle = {
    vertices: Tuple3<p5.Vector>;
    strokeColor: Tuple4<number>;
    fillColor: Tuple4<number>;
};

export const drawTriangle = (p: p5, triangle: Triangle) => {
    p.push();
    p.stroke(...triangle.strokeColor);
    p.fill(...triangle.fillColor);
    p.beginShape();
    triangle.vertices.forEach((vertex) => p.vertex(vertex.x, vertex.y));
    p.endShape('close');
    p.pop();
};
