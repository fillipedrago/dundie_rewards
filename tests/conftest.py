MARKER = """
integration: Mark integration tests
unit: Mark units tests
high: High Priority
medium: Medium Priority
low: Low Priority
"""
import pytest

def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)

@pytest.fixture(autouse=True)
def go_to_tmpdir(request): # injeção de dependencias
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield # protocolo de generators
