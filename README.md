# Skullcup

Requires the following stl files to be downloaded into this directory

- https://cults3d.com/en/3d-model/home/coffee-cup
- https://cults3d.com/en/3d-model/various/to-make-or-not-to-make

I would really like to be able to automate these downloads in a way which is congenial to whichever stl repository we are using.

Output is a file also in this directory called skullcup.stl

Usage:

    docker run -it -v .:/root pymesh/pymesh make

Work in progress, use FreeCAD to validate and 'repair' the model prior to printing:


    docker run -it -v .:/root amrit3701/freecad-cli python3 root/src/freecad_fix.py

See also:

- [Skullcup 3d model unboxing video](https://www.youtube.com/watch?v=ma1O-DAhuYg&t=1s)
