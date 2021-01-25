import redis


class ExecRedis():
    def _get_redis_conf(self):
        self.host = '10.100.3.225'
        self.port = '6380'
        self.db = 0
        self.password = '3ebc6626'

    def conn_redis(self):
        try:
            pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db, password=self.password)
            self.r = redis.StrictRedis(connection_pool=pool)
        except Exception as e:
            print("连接redis失败".format(e))

    # def parseInput(self, sType, key):
    #     if sType == 'zset':
    def deleteRedisKey(self, key):
        """
        删除redis中指定key的键值对
        """
        try:
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


