import requests


class RunMethod():
    """
    request方法
    """
    def post_main(self, url, param, data):
        r = requests.post(url=url, params=param, data=data)
        return r

    def get_main(self, url, param):
        r = requests.get(url=url, params=param)
        return r


