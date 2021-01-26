import json
import time

from common import request, prefixRedisData, get_sign, prefixSqlData
from common.read_file import ReadFile


class Login():
    request = request.RunMethod()
    sign = get_sign.Sign()
    sql = prefixSqlData.ExecSql()
    redis = prefixRedisData.ExecRedis()
    file = ReadFile()

    def __init__(self):
        self.rep_params = {}
        self.base_param = self.file.read_yaml('test_yaml_path')['shanpinApi']
        self.redis_key = self.file.read_yaml('redis_yaml_path')['shanpinApi']

        # 获取base_url
        self.base_url = self.base_param["base_url"]
        # 获取手机号码
        self.phonenum = self.base_param["account"]["jing_account"]

        # 获取登录相关的
        self.login = self.base_param["agent_login"]
        # 获取登录的请求方法
        self.login_method = self.login["login_method"]
        # 获取登录的url
        self.login_url = self.login["login_url"]

        # 获取验证码相关的参数
        self.sms = self.base_param["agent_sms_code"]
        # 获取发送验证码的请求方法
        self.sms_method = self.sms["sms_method"]
        # 获取发送验证码的url
        self.sms_url = self.sms["sms_url"]

        # 获取redis相关的参数
        brokerid = '85'
        self.keyArray = self.redis.get_redis_key(brokerid)

    def agent_login(self):
        """
        登录闪聘
        """
        # done:已经登录过，再执行就会报错，要进行数据清理，后续再完成
        # done : 这个yaml中使用变量的，以后通过写一个变量替换方法来完成，
        params = self.login["params"]
        data = self.login["data"]

        # 发送验证码
        self.send_phone_code()
        # 获取并替换掉验证码
        verifycode = self.get_verifycode(str(self.phonenum))
        self.rep_params['verifycode'] = str(verifycode)

        timestamp = int(round(time.time() * 1000))
        self.rep_params["timestamp"] = str(timestamp)

        # 该方法获取sign，并返回替换sign之后的参数
        params = self.sign.replace_sign(params, self.rep_params, data)
        # 获取url
        url = self.base_url + self.login_url
        # 发送请求
        r = self.request.run_main(self.login_method, url, params, self.rep_params, data)
        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
        # 数据清理-删除验证码60s时间限制以及发送次数限制
        self.redis.deleteRedisKey("shanpinApi", self.keyArray)
        return r

    def send_phone_code(self):
        """
        获取验证码
        """
        params = self.login["params"]
        data = self.sms["data"]
        timestamp = int(round(time.time() * 1000))
        self.rep_params["timestamp"] = str(timestamp)
        # 该方法获取sign，并返回替换sign之后的参数，data是在request方法中进行的变量替换
        params = self.sign.replace_sign(params, self.rep_params, data)
        # 获取url
        url = self.base_url + self.sms_url
        # 发送请求
        r = self.request.run_main(self.sms_method, url, params, self.rep_params, data)

        print(json.dumps(r.json(), ensure_ascii=False, indent=2))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        return r

    def get_verifycode(self, phonenum):
        sql = f'select top 1 content from smssendqueue where KeyNum = {phonenum} order by smsid desc'
        result = self.sql.exec_sql("shanpinApi", sql)
        message = str(result).split("，")
        # 获取验证码
        verifycode = message[0].split("：")[1]
        return verifycode

if __name__ == '__main__':
    test = Login()
    # test.send_phone_code()
    test.agent_login()
    # test.send_phone_code()


