
import math


def cartesianToPolar(x, y):
    radius = math.sqrt(x*x + y*y)
    theta = math.atan2(y, x)
    return radius, theta


def polarToCartesian(radius, theta):
    x = radius * math.cos(theta)
    y = radius * math.sin(theta)
    return x, y


def cartesianToSpherical(x, y, z):
    xy, phi = cartesianToPolar(x, y)
    radius, theta = cartesianToPolar(xy, z)
    return radius, theta, phi


def sphericalToCartesian(radius, theta, phi):
    z, xy = polarToCartesian(radius, theta)
    x, y = polarToCartesian(xy, phi)
    return x, y, z
