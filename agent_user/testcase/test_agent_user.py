from AgentUser.agent_manage import AgentManage


class TestUser:
    def setup(self):
        self.user = AgentManage()

    def test_add_agent(self):
        self.user.add_agent()

    def test_update_agent(self):
        self.user.update_agent()

    def test_get_agent_list(self):
        self.user.get_agent_list()
