import base64
import logging
import shelve
import time
from hashlib import md5

import redis

from common.prefixSqlData import ExecSql


class MethonTest():
    sql = ExecSql()
    root_logger = logging.getLogger()
    # print(f"root_logger.handlers:{logging.getLogger().handlers}")
    for h in root_logger.handlers[:]:
        root_logger.removeHandler(h)
    logging.basicConfig(level=logging.INFO)

    def getSign(self):
        logging.info("这是getSign方法")
        ts = time.time()
        timestamp = int(round(ts * 1000))
        param = {
                 'version': '100',
                 'brokerid': '',
                 'key': '',
                 'mobile': '18275691113',
                 'source': "pc",
                 'productname': "51mdd_agent_pc",
                 'timestamp': '1611119751830',
                 }
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
        print(token_md5)
        print(md5(token_md5.encode(encoding='UTF-8')).hexdigest())

    def md5_code(self):
        # 测试md5加密方法
        data = 'Shanghai'
        print(md5(data.encode(encoding='UTF-8')).hexdigest())
        print(data)

    def get_time(self):
        # 测试时间戳获取方法
        ts = time.time()
        # 获取的是毫秒级时间戳
        print(int(round(ts * 1000)))

    def save_cookie(self):
        # todo：这里先用shelve保存写死的cookie，然后获取, cookie可能会过期，或者可以从redis中获取cookie
        # 从数据库中取出cookie
        db = shelve.open("../datas/cookies")
        cookie = "4c9890042602c4764529116ee697a290"
        db['cookie'] = cookie
        db.close()

    def get_cookie(self):
        db = shelve.open("../datas/cookies")
        cookies = db['cookie']
        print(cookies)

    def get_photoBase64encode(self):
        with open("common/12.png", "rb") as f:
            img_data = f.read()
            base64_data = base64.b64encode(img_data)
            pic_str = base64_data.decode("utf-8")
            # print(type(base64_data))
            print(pic_str)

    def conn_redis(self):
        # 可以通过url来连接
        # url = 'redis://:foobared@localhost:6379/0'
        # pool = ConnectionPool.from_url(url)
        # redis = StrictRedis(connection_pool=pool)
        # 注意这里的db是0-15的数字，不是写为db0-db15，
        pool = redis.ConnectionPool(host='10.100.3.225', port='6380', db=0, password='3ebc6626')
        r = redis.StrictRedis(connection_pool=pool)
        # print(r)
        #
        id = 53
        # print(r.exists("agent_broker_login_200508:121"))
        # print(r.get(f'agent_recommendlist_recentdate_201105:{id}'))


        print(r.delete('agent_verifycode_err_total_200508:85'))

        # print(r.hdel('agent_verifycode_200508:85', 'id'))

    def generate_dict(self):
        params=['pageno', 'pagesize', 'keyword', 'jobarea', 'funtype', 'sorttype']
        test_cases = ['1', '12', "销售", '', '', '0']
        case_params={}
        for k, v in zip(params, test_cases):
            case_params[k] = v

    def get_sql(self):
        phonenum = '18909980000'
        sql = f'delete from t_agent_broker where brokerphonenum = {phonenum}'







if __name__ == '__main__':
    t = MethonTest()
    # get_cookie()
    # save_cookie()
    # md5_code()
    # t.getSign()
    # t.get_photoBase64encode()
    # t.conn_redis()
    t.generate_dict()
