import base64
import shelve
import time
from hashlib import md5


def getSign():
    ts = time.time()
    timestamp = int(round(ts * 1000))
    param = {
             'version': 100,
             'brokerid': '',
             'key': '',
             'mobile': 18275691113,
             'source': "pc",
             'productname': "51mdd_agent_pc",
             'timestamp': 1611119751830,
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

def md5_code():
    # 测试md5加密方法
    data = 'Shanghai'
    print(md5(data.encode(encoding='UTF-8')).hexdigest())
    print(data)

def get_time():
    # 测试时间戳获取方法
    ts = time.time()
    # 获取的是毫秒级时间戳
    print(int(round(ts * 1000)))

def save_cookie():
    # todo：这里先用shelve保存写死的cookie，然后获取, cookie可能会过期，或者可以从redis中获取cookie
    # 从数据库中取出cookie
    db = shelve.open("../datas/cookies")
    cookie = "4c9890042602c4764529116ee697a290"
    db['cookie'] = cookie
    db.close()

def get_cookie():
    db = shelve.open("../datas/cookies")
    cookies = db['cookie']
    print(cookies)

def get_photoBase64encode():
    with open("../common/12.png", "rb") as f:
        img_data = f.read()
        base64_data = base64.b64encode(img_data)
        pic_str = base64_data.decode("utf-8")
        # print(type(base64_data))
        print(pic_str)

if __name__ == '__main__':
    # getSign()
    # get_cookie()
    # save_cookie()
    # md5_code()
    get_photoBase64encode()
