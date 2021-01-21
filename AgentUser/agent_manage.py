import json
import time

import requests

from AgentUser.base_api import BaseApi


class AgentManage(BaseApi):
    def add_agent(self):
        """
        添加经纪人
        :return:
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
            "sign": ''
        }
        data = {
            "phonenum": 19122220002,
            "name": "测试",
        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign

        r = requests.post("https://shanpinapi.51job.com/user/add_broker.php",
                          params=params,
                          data=data)
        # r.encoding = "gbk"
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def update_agent(self):
        """
        编辑经纪人
        :return:
        """
        # todo:经纪人id、手机号码、姓名，要作为变量传入，在其他请求的响应中获取这个参数
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "version": 100,
            "productname": "51mdd_agent_pc",
            "brokerid": 87,
            "key": key,
            "timestamp": timestamp,
            "source": "pc",
            "sign": ''
        }
        data = {
            "phonenum": 19122220002,
            "name": "测试1",
            "editbroker": 120
        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign

        r = requests.post("https://shanpinapi.51job.com/user/add_broker.php",
                          params=params,
                          data=data)
        # r.encoding = "gbk"
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def get_agent_list(self):
        """
        获取经纪人列表
        :return:
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
            "sign": ''
        }
        data = {
            "pageno": 1,
            "pagesize": 10
        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign

        r = requests.post("http://shanpinapi.51job.com/user/get_broker_list.php",
                          params=params,
                          data=data)
        # r.encoding = "gbk"
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def change_agent_status(self):
        """
        禁用或解禁经纪人
        :return:
        """
        pass

    def member_join(self):
        """
        申请加入
        :return:
        """
        pass

    def get_unread_message(self):
        """
        获取是否有未读消息
        :return:
        """
        pass
