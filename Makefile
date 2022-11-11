install:
	poetry install
	
build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl
	
package-uninstall:
	python3 -m pip uninstall --yes dist/*.whl
	
gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage-html:
	poetry run pytest --cov=gendiff --cov-report=html:tests/tests_result

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/
