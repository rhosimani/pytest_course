import pytest

# To run test
# poetry run pytest -v -m webtest
# poetry run pytest -v -m "not webtest"

@pytest.mark.webtest
def test_send_http():
    pass

def test_something_quick():
    pass

def test_another():
    pass
