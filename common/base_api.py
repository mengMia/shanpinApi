import shelve
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
        conn = pymssql.connect(server, user, password, "sms", charset="GBK")  # 获取连接
        return conn

    def get_verifycode(self, phonenum):
        # done:手机号码作为变量传入
        # todo:不知道从数据库获取验证码的方式是否符合普通规则，毕竟线上是没法从数据库获取验证码的，上线之后怎么用这个用例验证呢
        # 调用conn_db方法获取conn
        self.cursor = self.conn_db().cursor()
        self.cursor.execute('select top 1 content from smssendqueue where KeyNum = %s order by smsid desc',
                            phonenum)
        message = str(self.cursor.fetchone()).split("，")
        # 获取验证码
        verifycode = message[0].split("：")[1]
        # print(type(code))
        return verifycode

    def get_sign(self, param_request, data_request):
        # ts = time.time()
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

        # 合并请求里的params和data传参
        param = {**param_request, **data_request}
        del param["sign"]
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
        # print(query)

        # md5加密
        key = "51job-signature-agent"
        token_md5 = (md5(query.encode(encoding='UTF-8')).hexdigest()) + key
        # print(token_md5)
        token = md5(token_md5.encode(encoding='UTF-8')).hexdigest()
        return token

    def get_cookie(self):
        # todo：这里先用shelve保存写死的cookie，然后获取, cookie可能会过期，或者可以从redis中获取cookie
        # 从数据库中取出cookie
        # testcase里面的测试用例调用这个方法，所以目录要先从testcase目录回到上一层，再进入datas找cookie
        db = shelve.open("../datas/cookies")
        cookies = db['cookie']
        db.close()
        return cookies


