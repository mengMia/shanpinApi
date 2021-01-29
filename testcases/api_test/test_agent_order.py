import pytest

from api.agent_order import AgentOrder
from common.read_file import ReadFile


class TestAgentOrder():
    # todo:难道每个测试用例都要传入key进去吗
    order = AgentOrder()
    file = ReadFile()
    api_data = file.read_yaml("order_yaml_path")["shanpinApi"]["order"]["list"]
    # print(type(api_data["test_keyword0"]))
    # data = api_data["test_keyword0"]

    @pytest.mark.parametrize('pageno, pagesize, keyword, jobarea, funtype, sorttype', [
        api_data["test_keyword0"]])
    def test_get_order_list(self, get_token, pageno, pagesize, keyword, jobarea, funtype, sorttype):
        key = get_token
        self.order.get_order_list(key, pageno, pagesize, keyword, jobarea, funtype, sorttype)

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