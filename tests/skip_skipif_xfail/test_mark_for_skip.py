import pytest

@pytest.mark.skip(reason="Skip for now")
def test_mark_for_skip():
    pass

def test_without_skip():
    pass
