import pytest

from api.agent_order import AgentOrder
from common.read_file import ReadFile


class TestAgentOrder():
    def setup(self):
        self.order = AgentOrder()
        self.file = ReadFile()

    def get_data(self):
        data = self.file.read_yaml("order_yaml_path")["shanpinApi"]
        return data

    @pytest.mark.parametrize('keyword', [
        "销售代表", "前台"
    ]
    )
    def test_get_order_list(self, keyword, **kwargs):
        self.order.get_order_list(keyword)

    def test_get_job_info(self):
        self.order.get_job_info()

    def test_get_share_image(self):
        self.order.get_share_image()

    def test_set_collection(self):
        self.order.set_collection()