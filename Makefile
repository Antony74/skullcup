all: working/cupWithoutHandle.stl

working/handle.stl: handle.py
	python3 handle.py

working/lip.stl: lip.py
	python3 lip.py

working/cup.stl: cup.py Coffee_Cup.A.1.stl
	python3 cup.py

working/cupWithoutHandle.stl: working/cup.stl working/handle.stl sub.py
	python3 sub.py working/cupWithoutHandle.stl working/cup.stl working/handle.stl

working/skull.stl: skullcup.py Scull_geant_fix02.stl
	python3 skullcup.py

clean:
	rm -rf working/*.stl
