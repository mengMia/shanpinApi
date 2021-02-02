import pymssql
import pymysql
import yaml

from common.log import Log
from common.read_file import ReadFile


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
    file = ReadFile()
    log = Log()

    def __init__(self):
        """
        初始化sqlserver配置
        :param platform_name:
        """
        self.sql_conf = None
        # with open('../config/test.yaml') as f:
        #     self.conf = yaml.safe_load(f)
        self.conf = self.file.read_yaml('test_yaml_path')

    def _get_sql_conf(self, project):
        try:
            return self.conf[project]['sql']
        except Exception as e:
            self.log.error("找不到项目:{0}".format(e))

    def conn_db(self, server):
        """
        连接sqlserver
        :return:
        """
        host = self.sql_conf[server]['host']  # 连接服务器地址
        user = self.sql_conf[server]['user']  # 连接帐号
        password = self.sql_conf[server]['pwd']  # 连接密码
        db = self.sql_conf[server]['db']  # 使用的数据库
        try:
            if server == 'sqlserver':
                self.conn = pymssql.connect(host, user, password, db, charset="GBK")  # 获取连接
            elif server == 'mysqlserver':
                self.conn = pymysql.connect(host=host, user=user, password=password, db=db, charset="GBK")
        except Exception as e:
            self.log.error("连接失败:{0}".format(e))

    def get_cursor(self):
        """
        获取游标
        """
        self.cursor = self.conn.cursor()
        return self.cursor

    def exec_sql(self, project, server, sql):
        # todo 仅仅写了执行查询语句，增删改还没封装
        # 获取sql配置
        self.sql_conf = self._get_sql_conf(project)
        try:
            # 使用已获取到的sql配置：sql_conf连接数据库
            self.conn_db(server)
            # 获取游标
            cursor = self.get_cursor()
            # 执行sql语句
            cursor.execute(sql)
            # 获取sql执行结果
            result = cursor.fetchone()
            self.cursor.close()
            self.conn.close()
            return result
        except Exception as e:
            self.log.error("执行sql语句出错".format(e))


if __name__ == '__main__':
    test = ExecSql()
    phonenum = 18275691111
    sql = f'select top 1 content from smssendqueue where KeyNum = {phonenum} order by smsid desc'
    result = test.exec_sql("shanpinApi", 'sqlserver', sql)
    print(result)



