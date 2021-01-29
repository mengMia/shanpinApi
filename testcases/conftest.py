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

file = ReadFile()
api_data = file.read_yaml("order_yaml_path")["shanpinApi"]["order"]["list"]
