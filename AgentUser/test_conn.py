import pymssql

from AgentUser.base_api import BaseApi


class TestConn(BaseApi):
    def setup(self):
        self.cursor = self.conn_db().cursor()

    def teardown(self):
        self.conn_db().close()

    def test_conn_db(self):
        # conn = pymssql.connect(host='10.100.2.142', user='sa', passwd='abc123!', db='sms', port=3306, charset='utf8')
        # conn = pymssql.connect(r'SERVER=10.100.2.142;UID=sa;PWD=abc123!;db=sms')
        # server = "10.100.2.142"  # 连接服务器地址
        # user = "sa"# 连接帐号
        # password = "abc123!" # 连接密码
        # conn = pymssql.connect(server, user, password, "sms")  # 获取连接

        # 查询该手机号的验证码记录
        self.cursor.execute('select top 1 content from smssendqueue where KeyNum = %s order by smsid desc', '18275691113')
        message = str(self.cursor.fetchone()).split("，")
        # 获取验证码
        code = message[0].split("：")[1]
        print(type(code))
        print(code)