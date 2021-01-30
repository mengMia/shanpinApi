# 方法名作为参数
import pytest

test_user_data = {
    'Tome': '123',
    'Jerry': '123',
}
@pytest.fixture(scope="module")
def login_r(request):
    # 通过request.param获取参数
    user = request.param
    print(f"\n 登录用户：{user}")
    return user

@pytest.mark.parametrize("login_r", test_user_data,indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login的返回值; {a}")
    assert a != ""