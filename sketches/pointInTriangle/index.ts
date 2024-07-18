import p5 from 'p5';
import { pointInSimplex } from '../../src/simplex';
import { drawTriangle, Triangle } from '../triangle';
import { draggableVertices } from '../draggableVertices';

new p5((p: p5) => {
    const width = 400;
    const height = 400;
    const vertexSize = 10;

    const vertices = [0, 1, 2, 3, 4, 5].map((index) => {
        const theta = p.map(index, 0, 6, 0, p.TWO_PI);
        return new p5.Vector(
            0.4 * width * Math.cos(theta),
            0.4 * height * Math.sin(theta)
        ).add(0.5 * width, 0.5 * height);
    });

    const getTriangle1 = (): Triangle => {
        return [vertices[0], vertices[2], vertices[4]];
    };

    const getTriangle2 = (): Triangle => {
        return [vertices[1], vertices[3], vertices[5]];
    };

    p.setup = () => {
        p.createCanvas(width, height);
        p.rectMode(p.RADIUS);
    };

    p.draw = () => {
        p.background(255);

        drawTriangle(p, getTriangle1(), [0, 255, 0, 128]);
        drawTriangle(p, getTriangle2(), [0, 0, 255, 128]);

        p.fill(255, 0, 0, 192);
        p.noStroke();
        vertices.forEach((v) => p.rect(v.x, v.y, vertexSize, vertexSize));

        p.noLoop();
    };

    draggableVertices({ p, vertices, vertexSize, width, height });
});
