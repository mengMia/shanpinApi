# import pytest
#
# from testcases.conftest import api_data
#
#
# @pytest.fixture(scope="function")
# def testcase_data(request):
#     print("----api_test/conftest----")
#     testcase_name = request.function.__name__
#     print(testcase_name)
#     return api_data.get(testcase_name)