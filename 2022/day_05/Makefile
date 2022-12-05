.SILENT:

test:
	python3 -m doctest -v solve.py

format:
	black *.py

lint:
	pylint *.py || true
	rm -rf ./__pycache__

solve:
	python3 ./solve.py
