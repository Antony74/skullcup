import p5 from 'p5';

new p5((p: p5) => {
    p.setup = () => {
        p.createCanvas(200, 200);
        p.background(255, 0, 0);
    };
});
