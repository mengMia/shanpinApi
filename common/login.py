import json
import time

import yaml

from common import request
from common import sign
from common import base_api

class Login():
    request = request.RunMethod()
    sign = sign.Sign()
    db = base_api.BaseApi()

    def __init__(self):
        with open("../config/test.yaml", encoding='utf-8') as f:
            self.base_param = yaml.safe_load(f)
        # 获取base_url
        self.base_url = self.base_param["shanpinApi"]["base_url"]
        # 获取手机号码
        self.phonenum = self.base_param["shanpinApi"]["account"]["jing_account"]
        # 获取登录的请求方法
        self.login_method = self.base_param["shanpinApi"]["agent_login"]["login_method"]
        # 获取登录的url
        self.login_url = self.base_param["shanpinApi"]["agent_login"]["login_url"]
        # 获取发送验证码的请求方法
        self.sms_url = self.base_param["shanpinApi"]["agent_sms_code"]["sms_method"]
        # 获取发送验证码的url
        self.sms_url = self.base_param["shanpinApi"]["agent_sms_code"]["sms_url"]
        # 从数据库获取验证码
        self.verifycode = self.get_verifycode(str(self.phonenum))


    def agent_login(self):
        # todo:已经登录过，再执行就会报错，要进行数据清理，后续再完成

        # todo : 这个yaml中使用变量的，以后通过其他办法解决，
        timestamp = int(round(time.time() * 1000))
        self.base_param["shanpinApi"]["agent_login"]["params"]["timestamp"] = timestamp

        # 获取并替换掉验证码
        verifycode = self.get_verifycode(str(self.phonenum))
        self.base_param["shanpinApi"]["agent_login"]["data"]["phonecode"] = verifycode
        params = self.base_param["shanpinApi"]["agent_login"]["params"]
        data = self.base_param["shanpinApi"]["agent_login"]["data"]

        # 获取并替换掉sign
        sign = self.sign.get_sign(params, data)
        params["sign"] = sign
        url = self.base_url + self.login_url

        # 发送请求
        r = self.request.run_main(self.login_method, url, params, data)
        print(json.dumps(r.json(), ensure_ascii=False, indent=2))

    def get_verifycode(self, phonenum):
        # done:手机号码作为变量传入
        # todo:不知道从数据库获取验证码的方式是否符合普通规则，毕竟线上是没法从数据库获取验证码的，上线之后怎么用这个用例验证呢
        # 调用conn_db方法获取conn
        self.cursor = self.db.conn_db().cursor()
        self.cursor.execute('select top 1 content from smssendqueue where KeyNum = %s order by smsid desc',
                            phonenum)
        message = str(self.cursor.fetchone()).split("，")
        # 获取验证码
        verifycode = message[0].split("：")[1]
        return verifycode

if __name__ == '__main__':
    test = Login()
    test.agent_login()


