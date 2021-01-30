import allure
import pytest

from api.agent_order import AgentOrder
from common.get_sign import Sign
from common.read_file import ReadFile


# @allure.step


class TestAgentOrder():
    # todo:难道每个测试用例都要传入key进去吗
    # todo:登录前也要做数据清理，清除验证码的redis
    order = AgentOrder()
    param = Sign()
    file = ReadFile()
    api_data = file.read_yaml("order_yaml_path")["shanpinApi"]["order"]
    # todo：可以放在conftest文件中吧
    base_param = file.read_yaml("test_yaml_path")["shanpinApi"]["base_params"]
    # print(api_data["test_cases"])

    @allure.story("用例--登录状态下获取订单列表")
    @pytest.mark.parametrize('get_testcases', api_data["get_order_list"]["test_cases"], indirect=True)
    def test_get_order_list(self, get_token, get_testcases):
        # todo:订单列表，是否登录，获取的列表不一样，用例还没设计
        # 通过传入函数名get_token调用fixture来获取登录key
        key = get_token
        # 通过传入函数名调用fixture来获取测试用例
        test_cases = get_testcases
        # 获取测试用例的参数之后，要把base_params进行变量替换，获取sign之后再传入接口
        brokerid = '85'
        params = self.param.get_requestparams(brokerid, key, test_cases, self.base_param, self.api_data["get_order_list"]["params"])
        self.order.get_order_list(params)

    @allure.story("用例--获取职位详情")
    @pytest.mark.parametrize('get_testcases', api_data["get_job_info"]["test_cases"], indirect=True)
    def test_get_job_info(self, get_token, get_testcases):
        key = get_token
        test_cases = get_testcases
        brokerid = '85'
        params = self.param.get_requestparams(brokerid, key, test_cases, self.base_param, self.api_data["get_job_info"]["params"])
        self.order.get_job_info(params)

#     def test_get_share_image(self):
#         self.order.get_share_image()
#
#     def test_set_collection(self):
#         self.order.set_collection()
#
if __name__ == '__main__':
    pytest.main("-v -s test_agent_order")
#     test = TestAgentOrder()
#     # test.get_data()