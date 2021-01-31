import allure
import pytest

from api.agent_order import AgentOrder
from common.get_sign import Sign
from common.log import Log
from common.read_file import ReadFile


# @allure.step


class TestAgentOrder():
    # todo:难道每个测试用例都要传入key进去吗
    # todo:登录前也要做数据清理，清除验证码的redis
    log = Log()
    order = AgentOrder()
    param = Sign()
    file = ReadFile()
    api_data = file.read_yaml("order_yaml_path")["shanpinApi"]["order"]
    # todo：可以放在conftest文件中吧
    base_param = file.read_yaml("test_yaml_path")["shanpinApi"]["base_params"]
    # print(api_data["test_cases"])

    @allure.story("用例--登录状态下获取订单列表")
    @pytest.mark.parametrize('test_cases', api_data["get_order_list"]["test_cases"], ids=api_data["get_order_list"]["ids"])
    def test_get_order_list(self, get_token, test_cases):
        # todo:订单列表，是否登录，获取的列表不一样
        # 通过传入函数名get_token调用fixture来获取登录key
        key = get_token
        # 获取测试用例的参数之后，要把base_params进行变量替换，获取sign之后再传入接口
        brokerid = '85'
        params = self.param.get_requestparams(brokerid, key, test_cases, self.base_param, self.api_data["get_order_list"]["params"])
        r = self.order.get_order_list(params)
        expect_result = self.api_data["get_order_list"]["expect_result"]
        assert r.status_code == expect_result[0]
        self.log.info("status ==> 期望结果:{}, 实际结果：【{}】".format(expect_result[1], r.json()['status']))
        assert r.json()['status'] == expect_result[1]
        assert r.json()['result'] == expect_result[2]
        self.log.info("*************测试用例执行结束****************")



    @allure.story("用例--获取职位详情")
    @pytest.mark.parametrize('test_cases', api_data["get_job_info"]["test_cases"], ids=api_data["get_job_info"]["ids"])
    def test_get_job_info(self, get_token, test_cases):
        key = get_token
        brokerid = '85'
        params = self.param.get_requestparams(brokerid, key, test_cases, self.base_param, self.api_data["get_job_info"]["params"])
        r = self.order.get_job_info(params)
        expect_result = self.api_data["get_job_info"]["expect_result"]
        assert r.status_code == expect_result[0]
        # 这个接口的status返回的竟然是字符串"1"
        assert r.json()['status'] == expect_result[1]
        assert r.json()['result'] == expect_result[2]

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