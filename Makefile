.PHONY: install virtualenv ipython clean test pflake8

install:
	@echo "Installing for dev enviroment"
	@.venv/Scripts/python -m pip install -e '.[dev]'

virtualenv:
	@.venv/Scripts/python -m pip -m venv .venv

ipython:
	@.venv/Scripts/ipython

lint:
	@.venv/Scripts/pflake8

test:
	@.venv/Scripts/pytest -s 

testci:
	@pytest -v --junitxml=test-result.xml

watch:
	@.venv/Scripts/ptw
