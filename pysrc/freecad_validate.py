import FreeCAD
import Mesh


def countDuplicatedFaces(filename):
    mesh = Mesh.Mesh(filename)
    countBefore = mesh.CountFacets
    mesh.removeDuplicatedFacets()
    countAfter = mesh.CountFacets
    return countBefore - countAfter

def countDuplicatedPoints(filename):
    mesh = Mesh.Mesh(filename)
    countBefore = mesh.CountPoints
    mesh.removeDuplicatedFacets()
    countAfter = mesh.CountPoints
    return countBefore - countAfter

def countDegeneratedFaces(filename):
    mesh = Mesh.Mesh(filename)
    countBefore = mesh.CountFacets
    mesh.fixDegenerations()
    countAfter = mesh.CountFacets
    return countBefore - countAfter

def hasBadFaceIndices(filename):
    mesh = Mesh.Mesh(filename)
    countBefore = mesh.CountFacets
    print(mesh.fixIndices())
    countAfter = mesh.CountFacets
    print(countBefore, countAfter)
    return countBefore != countAfter


def evaluateMesh(filename):
    print()
    print(filename)

    # object_methods = [method_name for method_name in dir(mesh)]
    # print('\n'.join(object_methods))

    mesh = Mesh.Mesh(filename)

    flippedNormals = mesh.countNonUniformOrientedFacets()
    print('Orientation: ' + str(flippedNormals) + ' flipped normals')

    duplicatedFaces = countDuplicatedFaces(filename)
    print('Duplicated faces: ' + str(duplicatedFaces))

    duplicatedPoints = countDuplicatedPoints(filename)
    print('Duplicated points: ' + str(duplicatedPoints))

    nonManifolds = mesh.hasNonManifolds()
    print('Non-manifolds: ' + str(nonManifolds))

    degenerations = countDegeneratedFaces(filename)
    print('Degenerated faces: ' + str(degenerations))

    # faceIndices = hasBadFaceIndices(filename)
    print('Face indices: ' + str('not implemented'))

    selfIntersections = mesh.hasSelfIntersections()
    print('Self-intersections: ' + str(selfIntersections))


evaluateMesh('root/mcup.stl')
evaluateMesh('root/skullcup.stl')

# Area
# BoundBox
# Content
# CountEdges
# CountFacets
# CountPoints
# Facets
# Matrix
# MemSize
# Module
# Placement
# Points
# Tag
# Topology
# TypeId
# Volume
# __class__
# __delattr__
# __dir__
# __doc__
# __eq__
# __format__
# __ge__
# __getattribute__
# __gt__
# __hash__
# __init__
# __init_subclass__
# __le__
# __lt__
# __ne__
# __new__
# __reduce__
# __reduce_ex__
# __repr__
# __setattr__
# __sizeof__
# __str__
# __subclasshook__
# addFacet
# addFacets
# addMesh
# clear
# coarsen
# collapseEdge
# collapseFacet
# collapseFacets
# copy
# countComponents
# countNonUniformOrientedFacets
# countSegments
# crossSections
# cut
# decimate
# difference
# dumpContent
# fillupHoles
# fixCaps
# fixDeformations
# fixDegenerations
# fixIndices
# fixSelfIntersections
# flipNormals
# foraminate
# getAllDerivedFrom
# getCurvaturePerVertex
# getEigenSystem
# getFacesFromSubelement
# getFacetSelection
# getInternalFacets
# getNonUniformOrientedFacets
# getPlanarSegments
# getPointNormals
# getPointSelection
# getSegment
# getSegmentsByCurvature
# getSegmentsOfType
# getSelfIntersections
# getSeparateComponents
# harmonizeNormals
# hasInvalidPoints
# hasNonManifolds
# hasNonUniformOrientedFacets
# hasSelfIntersections
# inner
# insertVertex
# intersect
# isDerivedFrom
# isSolid
# mergeFacets
# meshFromSegment
# nearestFacetOnRay
# offset
# offsetSpecial
# optimizeEdges
# optimizeTopology
# outer
# printInfo
# read
# rebuildNeighbourHood
# refine
# removeComponents
# removeDuplicatedFacets
# removeDuplicatedPoints
# removeFacets
# removeFoldsOnSurface
# removeFullBoundaryFacets
# removeInvalidPoints
# removeNeedles
# removeNonManifoldPoints
# removeNonManifolds
# restoreContent
# rotate
# setPoint
# smooth
# snapVertex
# splitEdge
# splitEdges
# splitFacet
# swapEdge
# transform
# transformToEigen
# translate
# trim
# unite
# write
# writeInventor
