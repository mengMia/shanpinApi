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

    def get_order_list(self, key, test_cases):
        """
        获取所有招聘订单列表
        :return:
        """
        # done: key使用conftest中的key进行获取
        timestamp = int(round(time.time() * 1000))
        # 将要替换的公共params参数存到rep_params中,
        # todo: 可以先在测试用例执行的地方替换好，把params参数传进来，
        #  这样request请求中不需要再进行替换了
        self.rep_params["timestamp"] = str(timestamp)
        self.rep_params["key"] = key
        self.rep_params["brokerid"] = '85'
        # done: 先调试获取登录key的
        # # 整合所有的params,test_case是每个用例传不同的参数
        case_params = {
            "pageno": test_cases[0],
            "pagesize": test_cases[1],
            "keyword": test_cases[2],
            "jobarea": test_cases[3],
            "funtype": test_cases[4],
            "sorttype": test_cases[5]
        }
        params = {**self.base_param, **case_params}
        # 获取sign并返回替换sign后的参数
        params = self.sign.replace_sign(params, self.rep_params)

        # 获取请求方式和url
        method = self.order_param["get_order_list"]["method"]
        url = self.order_param["get_order_list"]["url"]

        r = self.request.run_main(method, url, params, self.rep_params)
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def get_job_info(self, key):
        """
        获取订单详情-职位详情
        :return:
        """
        timestamp = int(round(time.time() * 1000))
        # key = self.get_cookie()
        params = {
            "orderid": 246,
            "version": 100,
            "productname": "51mdd_agent_pc",
            "brokerid": 85,
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
