import pytest

from api.agent_order import AgentOrder

class TestAgentOrder():
    # def setup(self):
    order = AgentOrder()

    # @pytest.mark.parametrize("keyword", api_data["test_keyword0"]["keyword"])
    def test_get_order_list(self, get_token):
        key = get_token
        self.order.get_order_list(key)

    def test_get_job_info(self):
        self.order.get_job_info()

    def test_get_share_image(self):
        self.order.get_share_image()

    def test_set_collection(self):
        self.order.set_collection()

# if __name__ == '__main__':
#     test = TestAgentOrder()
#     test.get_data()