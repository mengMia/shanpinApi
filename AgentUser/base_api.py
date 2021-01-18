
import pymssql

class BaseApi():
    def conn_db(self):
        # conn = pymssql.connect(host='10.100.2.142', user='sa', passwd='abc123!', db='sms', port=3306, charset='utf8')
        # conn = pymssql.connect(r'SERVER=10.100.2.142;UID=sa;PWD=abc123!;db=sms')
        server = "10.100.2.142"  # 连接服务器地址
        user = "sa"  # 连接帐号
        password = "abc123!"  # 连接密码
        conn = pymssql.connect(server, user, password, "sms", charset="GBK")  # 获取连接
        return conn