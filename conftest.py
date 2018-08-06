import pytest
from fixture.ApplicationTest import ApplicationTest

@pytest.fixture(scope = "session")
def app(request):
    fixture = ApplicationTest()
    request.addfinalizer(fixture.destroy)
    return fixture