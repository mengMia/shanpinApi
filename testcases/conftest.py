import json
import pytest
from common.login import Login
from common.read_file import ReadFile


@pytest.fixture(scope='session')
def get_token():
    """
    登录获取key并返回
    """
    r = Login().agent_login()
    print(json.dumps(r.json(), ensure_ascii=False, indent=2))
    get_token = r.json()['key']
    return get_token

@pytest.fixture(scope="function")
def get_testcases(request):
    # 通过request.param获取参数
    test_cases = request.param
    # print(f"\n 登录用户：{user}")
    return test_cases

# # 这个暂时没用，但是执行测试用例时会去加载D:\CS\PythonCode\testcases\api_test\conftest.py文件，这个文件中有导入api_data的语句，如果不写的话会报错
# # 可见执行测试用例的时候，即使不引用conftest，也会去先加载conftest文件
# file = ReadFile()
# api_data = file.read_yaml("order_yaml_path")["shanpinApi"]["order"]["list"]


