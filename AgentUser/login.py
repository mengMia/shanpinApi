import json
import requests
from AgentUser.base_api import BaseApi


class Login(BaseApi):
    # todo:获取验证码需要进行数据清理，因为会有个发送次数的上限。应该先验证获取验证码的功能没有问题，再进行其他功能的验证，需要进行数据清理
    # todo:验证码的测试用例后续再写
    def send_phone_code(self):
        r = requests.post("http://shanpinapi.51job.com/user/send_phone_code.php",
                          params={
                            "version": 100,
                            "productname": "51mdd_agent_pc",
                            "brokerid": '',
                            "key": '',
                            "timestamp": 1611119751830,
                            "source": "pc",
                            "sign": "4d4d40c2b23e37b3c61885fcd47ea95b"
                          },
                          data={
                              "mobile": 18275691113
                          }
                        )

        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        return r

    def login_agent(self):
        r = requests.post("http://shanpinapi.51job.com/user/login.php",
                          params={
                              "version": 100,
                              "productname": "51mdd_agent_pc",
                              "brokerid": '',
                              "key": '',
                              "timestamp": 1611131029593,
                              "source": "pc",
                              "sign": "968ba9acf47cf16da9de2a18ecfd1cde"
                          },
                          data={
                              "mobile": 18275691113,
                              "phonecode": 152938,
                              "source": "pc",
                          }
        )
        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
        return r

    def logout_agent(self):
        pass
