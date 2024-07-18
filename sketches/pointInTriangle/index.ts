import p5 from 'p5';
import { pointInSimplex } from '../../src/simplex';
import { drawTriangle, Triangle } from '../triangle';
import { tupleMap } from '../../src/tuples';

new p5((p: p5) => {
    const width = 400;
    const height = 400;

    const starMap = (index) => {
        const theta = p.map(index, 0, 6, 0, p.TWO_PI);
        return new p5.Vector(
            0.4 * width * Math.cos(theta),
            0.4 * height * Math.sin(theta)
        ).add(0.5 * width, 0.5 * height);
    };

    const triangle1: Triangle = {
        vertices: tupleMap<number, p5.Vector, 3>([0, 2, 4], starMap),
        strokeColor: [0, 0, 0, 0],
        fillColor: [0, 255, 255, 128],
    };

    const vertices = [0, 1, 2, 3, 4, 5].map((index) => {
        const theta = p.map(index, 0, 6, 0, p.TWO_PI);
        return new p5.Vector(
            0.4 * width * Math.cos(theta),
            0.4 * height * Math.sin(theta)
        ).add(0.5 * width, 0.5 * height);
    });

    p.setup = () => {
        p.createCanvas(width, height);
        p.rectMode(p.RADIUS);
    };

    p.draw = () => {
        p.background(255);

        drawTriangle(p, triangle1);

        p.fill(255, 0, 0, 192);
        p.noStroke();
        vertices.forEach((v) => p.rect(v.x, v.y, 10, 10));

        p.noLoop();
    };
});
