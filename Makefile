all: skullcup.stl working/m.stl

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

working/nib.stl: src/nib.py
	python3 src/nib.py

working/cupCenteredIgnoringHandle.stl: working/cup.stl working/cupWithoutHandle.stl src/cupCenteredIgnoringHandle.py
	python3 src/cupCenteredIgnoringHandle.py

working/profile.json: working/cupCenteredIgnoringHandle.stl src/getProfile.py
	python3 src/getProfile.py

working/m.stl: working/cupCenteredIgnoringHandle.stl working/nib.stl working/profile.json src/m.py
	python3 src/m.py
