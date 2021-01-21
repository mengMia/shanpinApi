from AgentOrder.agent_order import AgentOrder


class TestAgentOrder():
    def setup(self):
        self.order = AgentOrder()

    def test_get_order_list(self):
        self.order.get_order_list()