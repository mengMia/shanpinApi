from AgentUser.agent_salary import AgentSalary


class TestAgentSalary():
    def setup(self):
        self.salary = AgentSalary()

    def test_get_settle_list(self):
        self.salary.get_settle_list()

    def test_get_settle_detail(self):
        self.salary.get_settle_detail()
