from agent_user.agent_login import AgentLogin


class TestUserLogin:
    def setup(self):
        self.userLogin = AgentLogin()

    def test_send_phonecode(self):
        self.userLogin.send_phone_code()
        
    def test_login(self):
        self.userLogin.login_agent()