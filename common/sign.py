from hashlib import md5


class Sign():
    def get_sign(self, param_request, data_request):
        """
        根据传入的参数获取签名，更新请求的params
        """
        # logging.info("调用了getSign方法")
        # 合并请求里的params和data传参
        param = {**param_request, **data_request}
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
        # print(token_md5)
        token = md5(token_md5.encode(encoding='UTF-8')).hexdigest()
        return token