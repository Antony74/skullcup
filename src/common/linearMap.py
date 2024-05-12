# Further reading: https://antony74.github.io/p5-notebook/dist/src/in-praise-of-the-map-function.html


def linearMap(n, start1, stop1, start2, stop2):
    return ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2


def createMap2D(mapFnX, mapFnY):
    def map(n, start1, stop1, start2, stop2):
        return [
            mapFnX(n, start1, stop1, start2[0], stop2[0]),
            mapFnY(n, start1, stop1, start2[1], stop2[1]),
        ]

    return map


def createMap3D(mapFnX, mapFnY, mapFnZ):
    def map(n, start1, stop1, start2, stop2):
        return [
            mapFnX(n, start1, stop1, start2[0], stop2[0]),
            mapFnY(n, start1, stop1, start2[1], stop2[1]),
            mapFnZ(n, start1, stop1, start2[2], stop2[2]),
        ]

    return map


linearMap2D = createMap2D(linearMap, linearMap)
linearMap3D = createMap3D(linearMap, linearMap, linearMap)

def findIndex(arr, fn):
    for i,v in enumerate(arr):
        if fn(v): return i
    return -1

def segmentedMap(value, range1, range2, maps):
    if (len(range1) != len(range2)):
        raise Exception('segmentedMap range arrays not equal')

    n = findIndex(range1, lambda t: t > value)

    if n == 0:
        return range2[0]
    elif n == -1:
        return range2[len(range2) - 1]
    else:
        currentMap = maps[n - 1] if maps and maps[n - 1] else linearMap
        return currentMap(
            value,
            range1[n - 1],
            range1[n],
            range2[n - 1],
            range2[n],
        )
