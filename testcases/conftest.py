
import pytest

from common.login import Login


@pytest.fixture(scope='session')
def get_token():
    """
    登录获取key并返回
    """
    r = Login().agent_login()
    get_token = r.json()['key']
    return get_token
