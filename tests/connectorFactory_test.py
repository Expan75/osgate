import pytest

def test_invalid_protocol():
    with pytest.raises(Exception):
        raise Exception