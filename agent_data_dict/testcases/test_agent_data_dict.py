from agent_data_dict.agent_data_dict import AgentDataDict


class TestAgentDataDict():
    def setup(self):
        self.data_dict = AgentDataDict()

    def test_get_dd_area(self):
        self.data_dict.get_dd_area()

    def test_get_dd_functype(self):
        self.data_dict.get_dd_funtype()

    def test_get_dd_degree(self):
        self.data_dict.get_dd_degree()

    def test_get_dd_jobarea(self):
        self.data_dict.get_dd_jobarea()

    def test_get_dd_saltype(self):
        self.data_dict.get_dd_saltype()