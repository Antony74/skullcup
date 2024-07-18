import p5 from "p5";

export const draggableVertices = (p: p5, vertices: p5.Vector[], vertexSize: number) => {
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
            vertex.x = p.mouseX;
            vertex.y = p.mouseY;
            p.loop();
        }
    };
}