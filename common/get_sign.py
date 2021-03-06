import time
from hashlib import md5

from common.read_file import ReadFile


class Sign():
    file = ReadFile()
    # 成员变量
    rep_params = {}
    # param_request = {}
    # data_request = {}

    def get_requestparams(self, brokerid, key, test_cases, base_param, params):
        """
        传入base_param和测试用例的参数，进行变量替换并且获取sign之后返回最终的请求参数
        """
        # todo: 这个函数不知道放在哪个模块比较合适，暂时先放这里
        # test_cases是传入的所有query和data参数，但是params是分开了query和data请求的字段，所以可以通过两个的字段长度来把test_cases分成query和data两部分
        params_query = params["query"]
        params_data = params["data"]
        query = test_cases[:len(params_query)]
        data = test_cases[(len(params_query)):]

        timestamp = int(round(time.time() * 1000))
        # 将要替换的公共params参数存到rep_params中,
        self.rep_params["timestamp"] = str(timestamp)
        self.rep_params["key"] = key
        self.rep_params["brokerid"] = brokerid

        # 先对从yaml中传进来的param_request, data_request进行变量替换
        base_param = self.file.var_replace(base_param, self.rep_params)
        # 把传入的query用例参数组合成字典的形式
        case_query={}
        for k, v in zip(params_query, query):
            case_query[k] = v
        # 把传入的data用例参数组合成字典的形式
        case_data = {}
        for k, v in zip(params_data, data):
            case_data[k] = v
        # 所有的query参数
        param_request = {**base_param, **case_query}
        data_request = case_data
        # 获取sign，需要所有的query参数和data参数
        # todo:经过这一步之后，sign参数被删除了，所以下面不进行替换了，而是直接加一个键值对
        sign = self.get_sign(param_request, data_request)
        # 在params中增加key为sign的键值对
        param_request["sign"] = sign
        # 返回替换后的params参数
        return [param_request, data_request]

    def replace_sign(self, param_request, rep_params, data_request=None):
        """
        获取sign，并返回替换sign之后的参数
        """
        # 初始化传入的参数,get_sign()中要调用这个成员变量
        # self.rep_params = rep_params
        # self.param_request = param_request
        # self.data_request = data_request
        param_request = self.file.var_replace(param_request, rep_params)
        data_request = self.file.var_replace(data_request, rep_params)
        # 获取sign
        sign = self.get_sign(param_request, data_request)
        # 替换params中的sign
        rep_params["sign"] = sign
        param_request = self.file.var_replace(param_request, rep_params)

        # 返回替换后的params参数
        return [param_request, data_request]

    def get_sign(self, param_request, data_request=None):
        """
        根据传入的参数获取签名，更新请求的params
        """
        # logging.info("调用了getSign方法")

        # 合并请求里的params和data传参
        if data_request is None:
            param = param_request
        else:
            param = {**param_request, **data_request}
        # 去除参数中的sign再加密
        # todo:为什么这里删除sign之后，get_requestparams方法里的param_request也被改变了
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

        # md5加密
        key = "51job-signature-agent"
        token_md5 = (md5(query.encode(encoding='UTF-8')).hexdigest()) + key
        sign = md5(token_md5.encode(encoding='UTF-8')).hexdigest()
        return sign


