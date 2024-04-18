.PHONY:

install:
	@echo "Installing for dev enviroment"
	@.venv/bin/python -m pip install -e '.[dev]'

virtualenv:
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@.venv/bin/ipython

test:
	@.venv/bin/pytest -vv -s tests/

watch:
	@.venv/bin/ptw -- -vv -s tests/
