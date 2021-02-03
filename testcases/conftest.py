import json
import pytest

from common import prefixRedisData
from common.login import Login
from common.prefixSqlData import ExecSql
from common.read_file import ReadFile

@pytest.fixture(scope='session')
def get_token(delete_logininfo):
    """
    登录获取key并返回
    """
    r = Login().agent_login()
    print(json.dumps(r.json(), ensure_ascii=False, indent=2))
    get_token = r.json()['key']
    return get_token

@pytest.fixture(scope='session')
def delete_logininfo():
    """
    登录之前的数据清理，删除该账号已经登录的记录
    """
    redis = prefixRedisData.ExecRedis()
    brokerid = '85'
    keyArray = redis.get_redis_key(brokerid)
    redis.deleteRedisKey("shanpinApi", keyArray)


# 用来获取测试用例，传入test方法里
@pytest.fixture(scope="function")
def get_testcases(request):
    # 通过request.param获取参数
    test_cases = request.param
    # print(f"\n 登录用户：{user}")
    return test_cases

@pytest.fixture()
def delete_agent(request):
    """
    添加经纪人之前的数据清理
    """
    test_cases = request.param
    phonenum = test_cases[0]
    sql_conn = ExecSql()
    sql = f'delete from t_agent_broker where brokerphonenum = {phonenum}'
    sql_conn.exec_sql("shanpinApi", 'mysqlserver', sql, 'del')
    return test_cases




# # 这个暂时没用，但是执行测试用例时会去加载D:\CS\PythonCode\testcases\api_test\conftest.py文件，这个文件中有导入api_data的语句，如果不写的话会报错
# # 可见执行测试用例的时候，即使不引用conftest，也会去先加载conftest文件
# file = ReadFile()
# api_data = file.read_yaml("order_yaml_path")["shanpinApi"]["order"]["list"]

def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
