import json
import time

import requests
from AgentUser.base_api import BaseApi

class AgentLogin(BaseApi):
    # todo:获取验证码需要进行数据清理，因为会有个发送次数的上限。应该先验证获取验证码的功能没有问题，再进行其他功能的验证，需要进行数据清理
    # todo:验证码的测试用例后续再写
    def send_phone_code(self):
        # 根据请求的传参获取sign
        # todo 后面再进一步封装这个方法
        timestamp = int(round(time.time() * 1000))
        params = {
            "version": 100,
            "productname": "51mdd_agent_pc",
            "brokerid": '',
            "key": '',
            "timestamp": timestamp,
            "source": "pc",
            "sign": ''
        }
        data = {
            "mobile": 18275691113
        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign
        # 发送请求
        r = requests.post("http://shanpinapi.51job.com/user/send_phone_code.php",
                          params=params,
                          data=data
                        )

        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        return r

    def login_agent(self):
        # todo:已经登录过，再执行就会报错，要进行数据清理，后续再完成
        timestamp = int(round(time.time() * 1000))
        params = {
            "version": 100,
            "productname": "51mdd_agent_pc",
            "brokerid": '',
            "key": '',
            "timestamp": timestamp,
            "source": "pc",
            "sign": ''
        }
        # 获取验证码
        phonenum = 18275691113
        verifycode = super().get_verifycode(str(phonenum))
        data = {
            "mobile": phonenum,
            "phonecode": verifycode,
            "source": "pc"
        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign
        # 发送请求
        r = requests.post("http://shanpinapi.51job.com/user/login.php",
                          params=params,
                          data=data
        )
        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        return r

    def logout_agent(self):
        pass
