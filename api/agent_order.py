import json
import time

import requests

from common.base_api import BaseApi
from common.get_sign import Sign
from common.read_file import ReadFile
from common import request
from testcases.conftest import get_token



class AgentOrder(BaseApi):
    sign = Sign()
    request = request.RunMethod()
    file = ReadFile()
    base_param = file.read_yaml("test_yaml_path")["shanpinApi"]["base_params"]
    order_param = file.read_yaml("order_yaml_path")["shanpinApi"]["order"]
    rep_params = {}
    # key = get_token

    def get_order_list(self, key):
        """
        获取所有招聘订单列表
        :return:
        """
        # todo: key使用conftest中的key进行获取
        # key = self.get_cookie()
        # key = get_token
        # key = "3413264becd85fce685128fe4520190e"
        timestamp = int(round(time.time() * 1000))
        # 将要替换的公共params参数存到rep_params中
        self.rep_params["timestamp"] = str(timestamp)
        self.rep_params["key"] = key
        self.rep_params["brokerid"] = '85'
        # todo: 先调试获取登录key的
        # # 整合所有的params,testc_case是每个用例传不同的参数
        # params = {**self.base_param, **test_case}
        test_case = self.order_param["list"]["test_keyword0"]
        params = {**self.base_param, **test_case}
        # 获取sign并返回替换sign后的参数
        params = self.sign.replace_sign(params, self.rep_params)

        # 获取请求方式和url
        method = self.order_param["list"]["method"]
        url = self.order_param["list"]["url"]

        r = self.request.run_main(method, url, params, self.rep_params)
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def get_job_info(self):
        """
        获取订单详情-职位详情
        :return:
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "orderid": 246,
            "version": 100,
            "productname": "51mdd_agent_pc",
            "brokerid": 87,
            "key": key,
            "timestamp": timestamp,
            "source": "pc",
            "sign": ''
        }
        data = {
        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign

        r = requests.get("http://shanpinapi.51job.com/order/get_job_info.php",
                          params=params,
                          )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        # 这个接口的status返回的竟然是字符串"1"
        assert r.json()['status'] == "1"
        assert r.json()['result'] == 1
        return r

    def get_share_image(self):
        """
        获取职位分享图片
        :return:
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "jobid": 18237552,
            "version": 100,
            "productname": "51mdd_agent_pc",
            "brokerid": 87,
            "key": key,
            "timestamp": timestamp,
            "source": "pc",
            "sign": ''
        }
        data = {
        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign

        r = requests.get("http://shanpinapi.51job.com/order/get_share_image.php",
                          params=params,
                          )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        # 这个接口的status返回的竟然是字符串"1"
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def set_collection(self):
        """
        收藏订单
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "orderid": 246,
            "status": 1, # 1表示收藏，0表示取消收藏
            "version": 100,
            "productname": "51mdd_agent_pc",
            "brokerid": 87,
            "key": key,
            "timestamp": timestamp,
            "source": "pc",
            "sign": ''
        }
        data = {
        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign

        r = requests.get("http://shanpinapi.51job.com/order/set_collection.php",
                         params=params,
                         )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        # 这个接口的status返回的竟然是字符串"1"
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

if __name__ == '__main__':
    order = AgentOrder()
    order.get_order_list()
