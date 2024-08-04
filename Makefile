WATCH_COMMAND=poetry run uvicorn --reload --port=8000 src.main:app

watch:
	${WATCH_COMMAND}

test:
	poetry run pytest -x -n auto --dist loadscope

retest:
	poetry run pytest -lx --ff -n auto

cov:
	poetry run pytest --cov=src

update:
	poetry update

report:
	poetry run coverage run -m pytest
	poetry run coverage report
	poetry run coverage html
