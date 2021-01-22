from agent_order.agent_order import AgentOrder


class TestAgentOrder():
    def setup(self):
        self.order = AgentOrder()

    def test_get_order_list(self):
        self.order.get_order_list()

    def test_get_job_info(self):
        self.order.get_job_info()

    def test_get_share_image(self):
        self.order.get_share_image()

    def test_set_collection(self):
        self.order.set_collection()