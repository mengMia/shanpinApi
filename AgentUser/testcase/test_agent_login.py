from AgentUser.login import Login


class TestUserLogin:
    def setup(self):
        self.userLogin = Login()

    def test_send_phonecode(self):
        self.userLogin.send_phone_code()
        
    def test_login(self):
        self.userLogin.login_agent()