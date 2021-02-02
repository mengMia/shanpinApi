import allure
import pytest

from api.agent_manage import AgentManage
from common.get_sign import Sign
from common.log import Log
from common.read_file import ReadFile


class TestUser:
    log = Log()
    user = AgentManage()
    param = Sign()
    file = ReadFile()
    api_data = file.read_yaml("user_yaml_path")["shanpinApi"]["user"]
    # todo：可以放在conftest文件中吧
    base_param = file.read_yaml("test_yaml_path")["shanpinApi"]["base_params"]
    # test_cases = api_data["add_agent"]["test_cases"]

    # print(api_data["test_cases"])

    # @allure.story("用例--登录状态下获取订单列表")

    @pytest.mark.parametrize('test_cases', api_data["add_agent"]["test_cases"],
                             ids=api_data["add_agent"]["ids"])
    def test_add_agent(self, get_token, test_cases):
        key = get_token
        # 获取测试用例的参数之后，要把base_params进行变量替换，获取sign之后再传入接口
        brokerid = '85'
        [query, data] = self.param.get_requestparams(brokerid, key, test_cases, self.base_param,
                                              self.api_data["add_agent"]["params"])
        r = self.user.add_agent(query, data)
        expect_result = self.api_data["add_agent"]["expect_result"]
        assert r.status_code == expect_result[0]
        self.log.info("status ==> 期望结果:{}, 实际结果：【{}】".format(expect_result[1], r.json()['status']))
        assert r.json()['status'] == expect_result[1]
        assert r.json()['result'] == expect_result[2]
        self.log.info("*************测试用例执行结束****************")

    def test_update_agent(self):
        self.user.update_agent()

    def test_get_agent_list(self):
        self.user.get_agent_list()
