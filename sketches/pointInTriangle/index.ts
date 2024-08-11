import p5 from 'p5';
import { pointInSimplex } from '../../src/simplex';
import { drawTriangle, triangleAsTuples } from '../triangle';
import { draggableVertices } from '../draggableVertices';
import { memoizeBounded } from '../../src/memoize';
import { Tuple3 } from '../../src/tuples';

const pointInTriangle = memoizeBounded(pointInSimplex<2, 3>, 100);

enum VertexState {
    pending,
    inside,
    outside,
}

type Vertex = { vec: p5.Vector; state: VertexState };

new p5((p: p5) => {
    const width = 400;
    const height = 400;
    const vertexSize = 10;

    const vertices = [0, 1, 2, 3, 4, 5].map((index): Vertex => {
        const theta = p.map(index, 0, 6, 0, p.TWO_PI);
        return {
            vec: new p5.Vector(
                0.4 * width * Math.cos(theta),
                0.4 * height * Math.sin(theta),
            ).add(0.5 * width, 0.5 * height),
            state: VertexState.pending,
        };
    });

    const getTriangle1 = (): Tuple3<Vertex> => {
        return [vertices[0], vertices[2], vertices[4]];
    };

    const getTriangle2 = (): Tuple3<Vertex> => {
        return [vertices[1], vertices[3], vertices[5]];
    };

    p.setup = () => {
        p.createCanvas(width, height);
        p.rectMode(p.RADIUS);
    };

    p.draw = async () => {
        p.background(255);

        const tri1 = getTriangle1();
        const tri2 = getTriangle2();

        drawTriangle(p, tri1, [0, 255, 0, 128]);
        drawTriangle(p, tri2, [0, 0, 255, 128]);

        p.fill(255, 0, 0, 192);
        p.noStroke();

        for (const { vec, state } of vertices) {
            switch (state) {
                case VertexState.pending:
                    p.noFill();
                    p.stroke(128, 192);
                    break;
                case VertexState.inside:
                    p.fill(0, 255, 255, 192);
                    p.noStroke();
                    break;
                case VertexState.outside:
                    p.fill(255, 0, 0, 192);
                    p.noStroke();
                    break;
            }
            p.rect(vec.x, vec.y, vertexSize, vertexSize);
        }

        tri1.forEach((v) => {
            const result = pointInTriangle(triangleAsTuples(tri2), [
                v.vec.x,
                v.vec.y,
            ]);

            if (result instanceof Promise) {
                result.then(async () => {
                    await new Promise((resolve) => setTimeout(resolve, 100));
                    p.loop();
                });
            } else {
                v.state = result ? VertexState.inside : VertexState.outside;
                p.loop();
            }
        });

        p.noLoop();
    };

    draggableVertices({
        p,
        vertices: vertices.map((v) => v.vec),
        vertexSize,
        width,
        height,
    });
});
