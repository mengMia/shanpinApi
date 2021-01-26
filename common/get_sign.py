import time
from hashlib import md5

from common.read_file import ReadFile


class Sign():
    file = ReadFile()
    # 成员变量
    rep_params = {}
    param_request = {}
    data_request = {}

    def replace_sign(self, param_request, rep_params, data_request=None):
        """
        获取sign，并返回替换sign之后的参数
        """
        self.rep_params = rep_params
        # 获取时间戳，并放到需要进行变量替换的rep_params字典中，调用get_sign方法时会调用变量替换方法，把rep_params字典传入get——sign方法
        timestamp = int(round(time.time() * 1000))
        self.rep_params["timestamp"] = str(timestamp)
        self.param_request = param_request
        self.data_request = data_request
        # 获取sign
        sign = self.get_sign()
        # 替换params中的sign
        self.rep_params["sign"] = sign
        param_request = self.file.var_replace(param_request, rep_params)

        # 返回替换后的params参数
        return param_request

    def get_sign(self):
        """
        根据传入的参数获取签名，更新请求的params
        """
        # logging.info("调用了getSign方法")
        # # 先对从yaml中传进来的param_request, data_request进行变量替换
        param_request = self.file.var_replace(self.param_request, self.rep_params)
        data_request = self.file.var_replace(self.data_request, self.rep_params)

        # 合并请求里的params和data传参
        if (data_request is None):
            param = param_request
        else:
            param = {**param_request, **data_request}
        # 去除参数中的sign再加密
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


