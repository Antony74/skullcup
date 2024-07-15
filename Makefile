all: skullcup.stl mcup.stl typescript.play

clean:
	rm -rf working/*.stl

# Cup

working/handle.stl: pysrc/handle.py pysrc/common/AffineMatrix.py pysrc/common/helpers.py
	python3 pysrc/handle.py

working/lip.stl: pysrc/lip.py
	python3 pysrc/lip.py

working/cup.stl: pysrc/cup.py Coffee_Cup.A.1.stl pysrc/common/AffineMatrix.py pysrc/common/helpers.py pysrc/fix_mesh/fix_mesh_lite.py
	python3 pysrc/cup.py

working/cupWithoutHandle.stl: working/cup.stl working/handle.stl pysrc/difference.py
	python3 pysrc/difference.py working/cupWithoutHandle.stl working/cup.stl working/handle.stl

working/cupWithoutHandleOrLip.stl: working/cupWithoutHandle.stl working/lip.stl pysrc/difference.py
	python3 pysrc/difference.py working/cupWithoutHandleOrLip.stl working/cupWithoutHandle.stl working/lip.stl

working/convexHull.stl: working/cupWithoutHandleOrLip.stl pysrc/convexHull.py
	python3 pysrc/convexHull.py working/convexHull.stl working/cupWithoutHandleOrLip.stl

# Skullcup

working/skull.stl: pysrc/skull.py Scull_geant_fix02.stl working/cupWithoutHandle.stl pysrc/common/AffineMatrix.py pysrc/common/helpers.py pysrc/fix_mesh/fix_mesh_lite.py
	python3 pysrc/skull.py

working/skullWithoutLip.stl: working/skull.stl working/lip.stl pysrc/difference.py
	python3 pysrc/difference.py working/skullWithoutLip.stl working/skull.stl working/lip.stl

working/skullWithoutCup.stl: working/skullWithoutLip.stl working/convexHull.stl pysrc/difference.py
	python3 pysrc/difference.py working/skullWithoutCup.stl working/skullWithoutLip.stl working/convexHull.stl

working/skullWithCup.stl: working/skullWithoutCup.stl working/cup.stl pysrc/union.py
	python3 pysrc/union.py working/skullWithCup.stl working/skullWithoutCup.stl working/cup.stl

working/skullcupUnfixed.stl: working/skullWithCup.stl pysrc/skullcup.py
	python3 pysrc/skullcup.py

skullcup.stl: working/skullcupUnfixed.stl pysrc/fix_mesh_lite_cli.py pysrc/fix_mesh/fix_mesh_lite.py
	python3 pysrc/fix_mesh_lite_cli.py skullcup.stl working/skullcupUnfixed.stl

# M cup (a cup with the letter 'M' on it)

working/prism.stl: pysrc/prism.py pysrc/common/helpers.py
	python3 pysrc/prism.py

working/cupCenteredIgnoringHandle.stl: working/cup.stl working/cupWithoutHandle.stl working/convexHull.stl pysrc/cupCenteredIgnoringHandle.py
	python3 pysrc/cupCenteredIgnoringHandle.py

working/profile.json: working/cupCenteredIgnoringHandle.stl pysrc/getProfile.py pysrc/common/bandedMap.py pysrc/common/linearMap.py
	python3 pysrc/getProfile.py

working/m.stl: working/prism.stl working/profile.json pysrc/common/coordinates.py pysrc/m.py pysrc/test_coordinates.py
	python3 -m unittest pysrc/test_coordinates.py
	python3 pysrc/m.py

working/mWithoutCup.stl: working/m.stl working/cupCenteredIgnoringHandle.stl
	python3 pysrc/difference.py working/mWithoutCup.stl working/m.stl working/convexHullCenteredIgnoringHandle.stl

working/partialCup.stl: working/cupCenteredIgnoringHandle.stl pysrc/partialCup.py
	python3 pysrc/partialCup.py

working/extrudedCup.stl: working/partialCup.stl pysrc/extrude.py
	python3 pysrc/extrude.py working/extrudedCup.stl working/partialCup.stl

working/extrudedCup2.stl: working/extrudedCup.stl pysrc/extrude.py
	python3 pysrc/extrude.py working/extrudedCup2.stl working/extrudedCup.stl

working/extrudedCupFinal.stl: working/extrudedCup2.stl pysrc/union.py
	python3 pysrc/union.py working/extrudedCupFinal.stl working/extrudedCup.stl working/extrudedCup2.stl

working/mWithSurface.stl: working/mWithoutCup.stl working/extrudedCupFinal.stl pysrc/intersection.py
	python3 pysrc/intersection.py working/mWithSurface.stl working/mWithoutCup.stl working/extrudedCupFinal.stl

mcup.stl: working/mWithSurface.stl pysrc/mcup.py pysrc/skullcup.py package.json
	python3 pysrc/mcup.py

typescript.play: package.json src/index.ts simplexPlay.py
	python3 simplexPlay.py
	# npm start
