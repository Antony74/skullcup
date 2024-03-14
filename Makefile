all: working/skullWithCup.stl

working/handle.stl: handle.py
	python3 handle.py

working/lip.stl: lip.py
	python3 lip.py

working/cup.stl: cup.py Coffee_Cup.A.1.stl
	python3 cup.py

working/cupWithoutHandle.stl: working/cup.stl working/handle.stl sub.py
	python3 sub.py working/cupWithoutHandle.stl working/cup.stl working/handle.stl

working/skull.stl: skull.py Scull_geant_fix02.stl working/cupWithoutHandle.stl
	python3 skull.py

working/cupWithoutHandleOrLip.stl: working/cupWithoutHandle.stl working/lip.stl sub.py
	python3 sub.py working/cupWithoutHandleOrLip.stl working/cupWithoutHandle.stl working/lip.stl

working/convexHull.stl: working/cupWithoutHandleOrLip.stl convexHull.py
	python3 convexHull.py working/convexHull.stl working/cupWithoutHandleOrLip.stl

working/skullWithoutLip.stl: working/skull.stl working/lip.stl sub.py
	python3 sub.py working/skullWithoutLip.stl working/skull.stl working/lip.stl

working/skullWithoutCup.stl: working/skullWithoutLip.stl working/convexHull.stl sub.py
	python3 sub.py working/skullWithoutCup.stl working/skullWithoutLip.stl working/convexHull.stl

working/skullWithCup.stl: working/skullWithoutCup.stl working/cup.stl add.py
	python3 add.py working/skullWithCup.stl working/skullWithoutCup.stl working/cup.stl

clean:
	rm -rf working/*.stl
