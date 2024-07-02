# Skullcup

Requires the following stl files to be downloaded into this directory

- https://cults3d.com/en/3d-model/home/coffee-cup
- https://cults3d.com/en/3d-model/various/to-make-or-not-to-make

I would really like to be able to automate these downloads in a way which is congenial to whichever stl repository we are using.

Output is a file also in this directory called skullcup.stl

Usage:

    docker run -it -v .:/root pymesh/pymesh make

See also:

- [Skullcup 3d model unboxing video](https://www.youtube.com/watch?v=ma1O-DAhuYg&t=1s)

## M cup - Work in progress

A cup with a letter M on it is also partially produced by the above make file.  We finish it off with a FreeCAD script

    docker run -it -v .:/root amrit3701/freecad-cli python3 root/src/freecad_mcup.py

For some reason FreeCAD's Constructive Solid Geometry (CSG) engine produces valid .stl when combining primitive shapes, something all pymesh's engines fall short of.  This might be a biased observation, however, as it was made with FreeCAD's validator!

