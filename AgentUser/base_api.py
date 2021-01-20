import time
from hashlib import md5

import pymssql

class BaseApi():
    # todo：服务器和用户名作为变量传入
    # todo: 一个模块只建立一次数据库的连接
    def conn_db(self):
        # conn = pymssql.connect(host='10.100.2.142', user='sa', passwd='abc123!', db='sms', port=3306, charset='utf8')
        # conn = pymssql.connect(r'SERVER=10.100.2.142;UID=sa;PWD=abc123!;db=sms')
        server = "10.100.2.142"  # 连接服务器地址
        user = "sa"  # 连接帐号
        password = "abc123!"  # 连接密码
        self.conn = pymssql.connect(server, user, password, "sms", charset="GBK")  # 获取连接
        return self.conn

    # todo:手机号码作为变量传入
    def get_verifycode(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute('select top 1 content from smssendqueue where KeyNum = %s order by smsid desc',
                            '18275691113')
        message = str(self.cursor.fetchone()).split("，")
        # 获取验证码
        verifycode = message[0].split("：")[1]
        # print(type(code))
        return verifycode

    def get_sign(self, param):
        ts = time.time()
        # timestamp = int(round(ts * 1000))
        # param = {
        #     'version': 100,
        #     'brokerid': '',
        #     'key': '',
        #     'mobile': 18275691113,
        #     'source': "pc",
        #     'productname': "51mdd_agent_pc",
        #     'timestamp': timestamp,
        # }
        # 按key的字典序将param排序
        params = {}
        for i in sorted(param):
            params[i] = param[i]

        # 拼接几个请求参数，按照key1=value1&key2=value2的形式
        query = ''
        for k in params:
            if len(query) > 0:
                query += '&'
            query = query + k + '=' + str(params[k])
        print(query)

        # md5加密
        key = "51job-signature-agent"
        token_md5 = (md5(query.encode(encoding='UTF-8')).hexdigest()) + key
        # print(token_md5)
        token = md5(token_md5.encode(encoding='UTF-8')).hexdigest()
        return token
