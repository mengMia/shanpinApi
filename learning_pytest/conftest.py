import pytest


@pytest.fixture()
def get_testcases(request):
    test_cases = request.param
    return test_cases