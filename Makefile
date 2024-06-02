all: skullcup.stl working/mcup.stl

clean:
	rm -rf working/*.stl

# Cup

working/handle.stl: src/handle.py src/common/AffineMatrix.py src/common/helpers.py
	python3 src/handle.py

working/lip.stl: src/lip.py
	python3 src/lip.py

working/cup.stl: src/cup.py Coffee_Cup.A.1.stl src/common/AffineMatrix.py src/common/helpers.py
	python3 src/cup.py

working/cupWithoutHandle.stl: working/cup.stl working/handle.stl src/difference.py
	python3 src/difference.py working/cupWithoutHandle.stl working/cup.stl working/handle.stl

working/cupWithoutHandleOrLip.stl: working/cupWithoutHandle.stl working/lip.stl src/difference.py
	python3 src/difference.py working/cupWithoutHandleOrLip.stl working/cupWithoutHandle.stl working/lip.stl

working/convexHull.stl: working/cupWithoutHandleOrLip.stl src/convexHull.py
	python3 src/convexHull.py working/convexHull.stl working/cupWithoutHandleOrLip.stl

# Skullcup

working/skull.stl: src/skull.py Scull_geant_fix02.stl working/cupWithoutHandle.stl src/common/AffineMatrix.py src/common/helpers.py
	python3 src/skull.py

working/skullWithoutLip.stl: working/skull.stl working/lip.stl src/difference.py
	python3 src/difference.py working/skullWithoutLip.stl working/skull.stl working/lip.stl

working/skullWithoutCup.stl: working/skullWithoutLip.stl working/convexHull.stl src/difference.py
	python3 src/difference.py working/skullWithoutCup.stl working/skullWithoutLip.stl working/convexHull.stl

working/skullWithCup.stl: working/skullWithoutCup.stl working/cup.stl src/union.py
	python3 src/union.py working/skullWithCup.stl working/skullWithoutCup.stl working/cup.stl

skullcup.stl: working/skullWithCup.stl src/skullcup.py
	python3 src/skullcup.py

# M cup (WIP)

working/prism.stl: src/prism.py
	python3 src/prism.py

working/cupCenteredIgnoringHandle.stl: working/cup.stl working/cupWithoutHandle.stl src/cupCenteredIgnoringHandle.py
	python3 src/cupCenteredIgnoringHandle.py

working/profile.json: working/cupCenteredIgnoringHandle.stl src/getProfile.py src/common/bandedMap.py src/common/linearMap.py
	python3 src/getProfile.py

working/m.stl: working/prism.stl working/profile.json src/common/coordinates.py src/m.py src/test_coordinates.py
	python3 -m unittest src/test_coordinates.py
	python3 src/m.py

working/mWithoutCup.stl: working/m.stl working/cupCenteredIgnoringHandle.stl
	python3 src/difference.py working/mWithoutCup.stl working/m.stl working/convexHullCenteredIgnoringHandle.stl

working/partialCup.stl: working/cupCenteredIgnoringHandle.stl src/partialCup.py
	python3 src/partialCup.py

working/extrudedCup.stl: working/partialCup.stl src/extrude.py
	python3 src/extrude.py working/extrudedCup.stl working/partialCup.stl

working/extrudedCup2.stl: working/extrudedCup.stl src/extrude.py
	python3 src/extrude.py working/extrudedCup2.stl working/extrudedCup.stl

working/extrudedCupFinal.stl: working/extrudedCup2.stl src/union.py
	python3 src/union.py working/extrudedCupFinal.stl working/extrudedCup.stl working/extrudedCup2.stl

working/mWithSurface.stl: working/mWithoutCup.stl working/extrudedCupFinal.stl src/intersection.py
	python3 src/intersection.py working/mWithSurface.stl working/mWithoutCup.stl working/extrudedCupFinal.stl

working/mcup.stl: working/mWithSurface.stl src/mcup.py
	python3 src/mcup.py

