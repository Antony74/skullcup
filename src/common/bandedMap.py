
from common.linearMap import linearMap


def createBandedMap(bands, min, max):

    def getBand(value):
        return int(round(linearMap(value, min, max, -0.5, bands + 0.5)))

    def fromBand(band):
        return linearMap(band, -0.5, bands + 0.5, min, max)

    return getBand, fromBand
