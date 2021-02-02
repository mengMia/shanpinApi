import datetime

import redis
import yaml

from common.read_file import ReadFile


class ExecRedis():
    file = ReadFile()
    def __init__(self):
        self.redis_conf = None

    def _get_redis_conf(self, project):
        """
        获取redis-server需要的参数
        """
        # with open('../config/test.yaml') as f:
        #     conf = yaml.safe_load(f)
        conf = self.file.read_yaml("test_yaml_path")
        self.redis_conf = conf[project]['sql']['redisserver']
        return self.redis_conf

    def conn_redis(self):
        """
        连接redis
        """
        host = self.redis_conf['host']
        port = self.redis_conf['port']
        db = self.redis_conf['db']
        password = self.redis_conf['password']
        try:
            pool = redis.ConnectionPool(host=host, port=port, db=db, password=password)
            self.r = redis.StrictRedis(connection_pool=pool)
            return self.r
        except Exception as e:
            print("连接redis失败".format(e))

    def get_redis_key(self, brokerid):
        """
        根据传入的经纪人id，获取对应的redis-key
        """
        redis_key = self.file.read_yaml('redis_yaml_path')['shanpinApi']
        keyArray = []
        for namespace in redis_key:
            if namespace == "agent-verifycode" or  namespace == 'agent-verifycode-err-total':
                key = redis_key[namespace]['prefix'] + "_" + redis_key[namespace]['timestamp'] + ":" + brokerid
                keyArray.append(key)
            elif namespace == 'agent-verifycode-total':
                key = redis_key[namespace]['prefix'] + "_" + redis_key[namespace]['timestamp'] + ":" + brokerid + "|" \
                + datetime.date.today().strftime('%Y%m%d')  #这里先用当天的日期，实际上应该拼接的是登录redis中的日期
                keyArray.append(key)
        return keyArray

    # def parseInput(self, sType, key):
    #     if sType == 'zset':
    def execRedis(self, project):
        """
        连接redis并返回数据库
        """
        self._get_redis_conf(project)
        self.r = self.conn_redis()
        return self.r

    def deleteRedisKey(self, project, keyArray):
        """
        删除redis中指定key的键值对
        """
        self.r = self.execRedis(project)
        try:
            for key in keyArray:
                self.r.delete(key)
        except Exception as e:
            print(e)

    def deleteRedisZset(self):
        """
        删除redis中的有序集合
        """
        pass

    def deleteRedisString(self):
        """
        删除redis中的字符串
        """

if __name__ == '__main__':
    test = ExecRedis()
    keyArray = ['agent_verifycode_200508:87', 'agent_verifycode_total_200508:87|20210125',
                         'agent_verifycode_err_total_200508:87']
    # test.deleteRedisKey(keyArray)
    test.deleteRedisKey("shanpinApi", keyArray)


