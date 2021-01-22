import json
import time

import requests

from common.base_api import BaseApi


class AgentCandidate(BaseApi):
    def recommend_resume(self):
        """
        推荐候选人
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
            "candidatephonenum": 18900002221,
            "candidatename": "麦子",
            "candidategender": 0,
            "candidatebirthday": "2021 - 01",
            "area": "050500",
            "candidatetopdegree": 3,
            "jobstatus": 1,
            "candidatestartworkyear": 2020,
            "currentsalary": "04",
            "currentsalarydesc": "是否",
            "expectsalarydesc": "返费",
            "expectsalary": "02",
            "entrytime": 1,
            "candidateemail": "223@aa.com",
            "tmpphotoname":'',
            "jobwantedintention":"地方",
            "recommendreason": '',
            "workdesc":"辅导费",
            "edudesc": "大幅度发",
            "additionaldesc": "大幅度",
            "tmpattachfiles": "",
            "resumetemplate":0,
            "resumeid": '',
            "recommendid":'',
            "orderid": 95,
            "resumefile":'',
        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign

        r = requests.post("http://shanpinapi.51job.com/candidate/recommend_resume.php",
                          params=params,
                          data=data
                         )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        # 这个接口的status返回的竟然是字符串"1"
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def update_recommend_resume(self):
        pass