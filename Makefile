.PHONY:

install:
	@echo "Installing for dev enviroment"
	@.venv/Scripts/python -m pip install -e '.[dev]'

virtualenv:
	@.venv/Scripts/python -m pip -m venv .venv

ipython:
	@.venv/Scripts/ipython

test:
	@.venv/Scripts/pytest -s 

testci:
	@pytest -v --junitxml=test-result.xml

watch:
	@.venv/Scripts/ptw
