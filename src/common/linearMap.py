# Further reading: https://antony74.github.io/p5-notebook/dist/src/in-praise-of-the-map-function.html


def linearMap(n, start1, stop1, start2, stop2):
    return ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2


def vector3Map(n, start1, stop1, start2, stop2):
    return [
        linearMap(n, start1, stop1, start2[0], stop2[0]),
        linearMap(n, start1, stop1, start2[1], stop2[1]),
        linearMap(n, start1, stop1, start2[2], stop2[2]),
    ]


def segmentedMap(value, range1, range2, maps):
    if (len(range1) != len(range2)):
        raise Exception('segmentedMap range arrays not equal')

    n = range1.findIndex(lambda t: t > value)

    if n == 0:
        return range2[0]
    elif n == -1:
        return range2[range2.length - 1]
    else:
        currentMap = maps and maps[n - 1] if maps[n - 1] else map
        return currentMap(
            value,
            range1[n - 1],
            range1[n],
            range2[n - 1],
            range2[n],
        )
