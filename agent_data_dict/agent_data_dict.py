import json
import time

import requests

from common.base_api import BaseApi


class AgentDataDict(BaseApi):
    def get_dd_area(self):
        """
        获取订单搜索的地区列表
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "version": 100,
            "productname": "51mdd_agent_pc",
            "brokerid": 87,
            "key": key,
            "timestamp": timestamp,
            "source": "pc",
            "sign": '',
        }
        data = {

        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign

        r = requests.get("http://shanpinapi.51job.com/datadict/get_dd_area.php",
                         params=params,
                         # data=data
                         )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def get_dd_funtype(self):
        """
        获取订单搜索的职能列表
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "version": 100,
            "productname": "51mdd_agent_pc",
            "brokerid": 87,
            "key": key,
            "timestamp": timestamp,
            "source": "pc",
            "sign": '',
        }
        data = {

        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign

        r = requests.get("http://shanpinapi.51job.com/datadict/get_dd_funtype.php",
                         params=params,
                         # data=data
                         )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def get_dd_degree(self):
        """
        获取填写简历时的学位字典
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "version": 100,
            "productname": "51mdd_agent_pc",
            "brokerid": 87,
            "key": key,
            "timestamp": timestamp,
            "source": "pc",
            "sign": '',
        }
        data = {

        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign

        r = requests.get("http://shanpinapi.51job.com/datadict/get_dd_degree.php",
                         params=params,
                         # data=data
                         )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def get_dd_jobarea(self):
        """
        获取工作地区
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "version": 100,
            "productname": "51mdd_agent_pc",
            "brokerid": 87,
            "key": key,
            "timestamp": timestamp,
            "source": "pc",
            "sign": '',
        }
        data = {

        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign

        r = requests.get("http://shanpinapi.51job.com/datadict/get_dd_jobarea.php",
                         params=params,
                         # data=data
                         )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def get_dd_saltype(self):
        """
        获取月薪
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "version": 100,
            "productname": "51mdd_agent_pc",
            "brokerid": 87,
            "key": key,
            "timestamp": timestamp,
            "source": "pc",
            "sign": '',
        }
        data = {

        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign

        r = requests.get("http://shanpinapi.51job.com/datadict/get_dd_saltype.php",
                         params=params,
                         # data=data
                         )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r