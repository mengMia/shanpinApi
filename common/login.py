import datetime
import json
import time

import yaml

from common import request, prefixRedisData, sign, prefixSqlData
from common.read_file import ReadFile


class Login():
    request = request.RunMethod()
    sign = sign.Sign()
    sql = prefixSqlData.ExecSql()
    redis = prefixRedisData.ExecRedis()
    file = ReadFile()

    def __init__(self):
        self.replace_params = {}
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
        self.sms_url = self.sms["sms_method"]
        # 获取发送验证码的url
        self.sms_url = self.sms["sms_url"]

        # 获取redis相关的参数
        brokerid = '85'
        self.keyArray = self.redis.get_redis_key(brokerid)

    def agent_login(self):
        # done:已经登录过，再执行就会报错，要进行数据清理，后续再完成
        # todo : 这个yaml中使用变量的，以后通过写一个变量替换方法来完成，
        params = self.login["params"]
        data = self.login["data"]
        # 获取并替换时间戳
        timestamp = int(round(time.time() * 1000))
        params["timestamp"] = timestamp

        # 发送验证码
        self.send_phone_code()
        # 获取并替换掉验证码
        verifycode = self.get_verifycode(str(self.phonenum))
        data["phonecode"] = verifycode
        # self.replace_params['timestamp'] = str(timestamp)
        # self.replace_params['phonecode'] = str(verifycode)
        # self.file.var_replace(params, self.replace_params)
        # self.file.var_replace(data, self.replace_params)

        # 获取并替换掉sign
        sign = self.sign.get_sign(params, data)
        params["sign"] = sign
        url = self.base_url + self.login_url

        # 发送请求
        r = self.request.run_main(self.login_method, url, params, data)
        print(json.dumps(r.json(), ensure_ascii=False, indent=2))

        # 数据清理-删除验证码60s时间限制以及发送次数限制
        self.redis.deleteRedisKey("shanpinApi", self.keyArray)

        return r

    def send_phone_code(self):
        # 根据请求的传参获取sign
        # todo 后面再进一步封装这个方法
        params = self.login["params"]
        data = self.sms["data"]
        # 获取并替换时间戳
        timestamp = int(round(time.time() * 1000))
        params["timestamp"] = timestamp

        # 获取并替换掉sign
        sign = self.sign.get_sign(params, data)
        params["sign"] = sign
        url = self.base_url + self.sms_url

        # 发送请求
        r = self.request.post_main(url, params, data)

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
    test.agent_login()
    # test.send_phone_code()


