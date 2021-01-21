import json
import time

import requests

from AgentUser.base_api import BaseApi


class AgentOrder(BaseApi):
    def get_order_list(self):
        """
        获取所有招聘订单列表
        :return:
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "pageno":1,
            "pagesize": 12,
            "keyword": '',
            "jobarea": '',
            "funtype": '',
            "sorttype": 0,
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

        r = requests.post("http://shanpinapi.51job.com/order/get_order_list.php",
                          params=params,
                          data=data
                          )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r