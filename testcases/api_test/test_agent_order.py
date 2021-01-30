import pytest

from api.agent_order import AgentOrder
from common.read_file import ReadFile
from testcases.conftest import get_testcases


class TestAgentOrder():
    # todo:难道每个测试用例都要传入key进去吗
    order = AgentOrder()
    file = ReadFile()
    api_data = file.read_yaml("order_yaml_path")["shanpinApi"]["order"]["get_order_list"]
    print(api_data["test_cases"])

    @pytest.mark.parametrize('get_testcases', api_data["test_cases"], indirect=True)
    def test_get_order_list(self, get_token, get_testcases):
        key = get_token
        test_cases = get_testcases
        self.order.get_order_list(key, test_cases)

    def test_get_job_info(self, get_token):
        key = get_token
        self.order.get_job_info(key)

    def test_get_share_image(self):
        self.order.get_share_image()

    def test_set_collection(self):
        self.order.set_collection()

if __name__ == '__main__':
    test = TestAgentOrder()
    # test.get_data()