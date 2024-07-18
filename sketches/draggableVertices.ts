import p5 from 'p5';

export const draggableVertices = ({
    p,
    vertices,
    vertexSize,
    width,
    height,
}: {
    p: p5;
    vertices: p5.Vector[];
    vertexSize: number;
    width: number;
    height: number;
}) => {
    let dragIndex = -1;

    p.mousePressed = () => {
        for (const index in vertices) {
            const vertex = vertices[index];
            if (
                Math.abs(p.mouseX - vertex.x) <= vertexSize &&
                Math.abs(p.mouseY - vertex.y) <= vertexSize
            ) {
                dragIndex = parseInt(index);
                return;
            }
        }

        dragIndex = -1;
    };

    p.mouseDragged = () => {
        const vertex = vertices[dragIndex];
        if (vertex) {
            vertex.x = Math.max(0, Math.min(p.mouseX, width));
            vertex.y = Math.max(0, Math.min(p.mouseY, height));
            p.loop();
        }
    };
};
