import json
import time

import requests

from AgentUser.base_api import BaseApi


class AgentSalary(BaseApi):
    def get_settle_list(self):
        """
        获取结算单列表
        :return:
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "pageno": 1,
            "pagesize": 10,
            "type": 0,
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

        r = requests.post("http://shanpinapi.51job.com/user/get_settle_list.php",
                          params=params
                          )
        # r.encoding = "gbk"
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def get_settle_detail(self):
        """
        获取结算单明细
        :return:
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "pageno": 1,
            "pagesize": 10,
            "settleid": 20210107140001,
            "type": 0,
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

        r = requests.post("http://shanpinapi.51job.com/user/get_settle_detail.php",
                          params=params
                          )
        # r.encoding = "gbk"
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

