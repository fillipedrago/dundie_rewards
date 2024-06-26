import pytest

from dundie.core import load
from tests.constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_2_people():
    """Test load function."""
    assert len(load(PEOPLE_FILE)) == 3


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_first_name_starts_with_J():
    """Test load function."""
    assert load(PEOPLE_FILE)[0]["name"] == "Jim Halpert"
