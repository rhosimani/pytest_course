import pytest
import sys

@pytest.mark.skipif(
    sys.version_info < (3, 10),
    reason="The version of python is less than 3.10"
)
def test_mark_for_skipif():
    pass

def test_without_skipif():
    pass

my_mark = pytest.mark.skipif(sys.version_info < (3, 10), reason="The version of python is less than 3.10")

@my_mark
def test_mark_with_mymark():
    pass
