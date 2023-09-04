import pytest

@pytest.mark.xfail()
def test_mark_for_xfail_and_raise_error():
    raise Exception("If the test was not marked with Xfail would produce an error.")

@pytest.mark.xfail()
def test_mark_for_xfail_without_error():
    pass

def test_without_xfail_and_raise_error():
    raise Exception("If the test was not marked with Xfail would produce an error.")

