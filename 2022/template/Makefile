.SILENT:

test:
	python3 -m doctest -v solve.py

format:
	find . -type f -name "*.py" | xargs black

lint:
	find . -type f -name "*.py" | xargs pylint 
	rm -rf ./__pycache__

solve:
	python3 ./solve.py

clean:
	find . -name '__pycache__' -exec rm -rf {} \+ || true
