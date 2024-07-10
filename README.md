# Skullcup

Requires the following stl files to be downloaded into this directory

- https://cults3d.com/en/3d-model/home/coffee-cup
- https://cults3d.com/en/3d-model/various/to-make-or-not-to-make

I would really like to be able to automate these downloads in a way which is congenial to whichever stl repository we are using.

Output is a file also in this directory called skullcup.stl

## Usage

    docker run -it -v .:/root pymesh/pymesh make

## Mesh validation

We can validate our models using the freecad-cli with the following Docker command, but note we do not attempt to fix them in an automated fashion, as this does not always have the desired consequence.

    docker run -it -v .:/root amrit3701/freecad-cli python3 root/pysrc/freecad_validate.py

## See also

- [Skullcup 3d model unboxing video](https://www.youtube.com/watch?v=ma1O-DAhuYg&t=1s)
