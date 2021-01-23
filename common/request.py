import requests


class RunMethod():
    """
    request方法
    """
    def post_main(self, url, param, data):
        """
        post请求
        """
        r = requests.post(url=url, params=param, data=data)
        return r

    def get_main(self, url, param):
        """
        get请求
        """
        r = requests.get(url=url, params=param)
        return r

    def run_main(self, method, url, params=None, data=None):
        """
        被调用主request
        """
        try:
            if method == 'post' or method == 'POST' or method == 'Post':
                r = self.post_main(url, params, data)
            elif method == 'get' or method == 'GET' or method == 'Get':
                r = self.get_main(url, params)
            else:
                return "request传参错误"
            return r
        except Exception as e:
            print("请求方法报错")




