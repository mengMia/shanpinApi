import pymssql
import yaml


class ExecSql():
    """
    执行sql语句类
    """
    # 缺一个日志类

    # 这部分代码不知道什么用处
    # _instance = None

    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance

    def __init__(self):
        """
        初始化sqlserver配置
        :param platform_name:
        """
        #
        # self.sql_conf = self._get_sql_conf(plarform_name)
        self.sql_conf = None
        with open('../config/test.yaml') as f:
            self.conf = yaml.safe_load(f)

    def _get_sql_conf(self, project):
        try:
            return self.conf[project]["sqlserver"]
        except Exception as e:
            print("找不到项目".format(e))

    def conn_db(self):
        """
        连接sqlserver
        :return:
        """
        server = self.sql_conf['host']  # 连接服务器地址
        user = self.sql_conf['user']  # 连接帐号
        password = self.sql_conf['pwd']  # 连接密码
        sms_db = self.sql_conf['sms_db']  # 使用的数据库
        try:
            self.conn = pymssql.connect(server, user, password, sms_db, charset="GBK")  # 获取连接
        except Exception as e:
            print("连接失败".format(e))

    def get_cursor(self):
        """
        获取游标
        """
        self.cursor = self.conn.cursor()
        return self.cursor

    def exec_sql(self, project, sql):
        # todo 仅仅写了执行查询语句，增删改还没封装
        self.sql_conf = self._get_sql_conf(project)
        self.conn_db()
        cursor = self.get_cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        self.cursor.close()
        self.conn.close()
        return result


if __name__ == '__main__':
    test = ExecSql()
    phonenum = 18275691111
    sql = f'select top 1 content from smssendqueue where KeyNum = {phonenum} order by smsid desc'
    result = test.exec_sql("shanpinApi", sql)
    print(result)



