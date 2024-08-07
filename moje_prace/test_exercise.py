import pytest

from exercise import *
@pytest.mark.parametrize("string, result", [("highline", "ihie"),
                                            ("policista", "oiit"),
                                            ((123456789), (2, 4, 6, 8))])
def test_odd_indexes(string, result):
    assert odd_indexes(string)
