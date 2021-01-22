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
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def update_recommend_resume(self):
        """
        修改候选人的简历
        """
        pass

    def check_has_resume(self):
        """
        检查是否推荐过候选人
        """
        # todo:这个逻辑还要再封装一下，有好几个返回结果
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "candidatephonenum": 18900002222,
            "orderid" : 95,
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

        r = requests.get("http://shanpinapi.51job.com/candidate/check_has_resume.php",
                          params=params,
                          # data=data
                          )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        # assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def get_candidate_list(self):
        """
        获取推荐的候选人列表
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "keyword":'',
            "fromdate": 2020 - 12 - 23,
            "todate": 2021 - 1 - 22,
            "auditstatus":'',
            "pageno":1,
            "pagesize":12,
            "filterbroker":'',
            "orderby":"updatedate",
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

        r = requests.get("https://shanpinapi.51job.com/candidate/get_candidate_list.php",
                         params=params,
                         # data=data
                         )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def get_resume_detail(self):
        """
        获取简历详情，简历审核不通过，需要重新修改的时候会调用这个接口
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "resumeid": 251,
            "recommendid": 395,
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

        r = requests.get("https://shanpinapi.51job.com/candidate/get_resume_detail.php",
                         params=params,
                         # data=data
                         )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def upload_photo(self):
        """
        上传图片
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        photo = self.get_photoBase64encode()
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
            "photo": photo
        }
        # 获取sign
        sign = self.get_sign(params, data)
        params["sign"] = sign

        r = requests.post("https://shanpinapi.51job.com/candidate/upload_photo.php",
                         params=params,
                         data=data
                         )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

    def remind_stage_audit(self):
        """
        提醒返费阶段审核
        """
        timestamp = int(round(time.time() * 1000))
        key = self.get_cookie()
        params = {
            "auditid": 897,
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

        r = requests.get("https://shanpinapi.51job.com/candidate/remind_stage_audit.php",
                         params=params,
                         # data=data
                         )
        print((json.dumps(r.json(), indent=2, ensure_ascii=False)))
        assert r.status_code == 200
        assert r.json()['status'] == 1
        assert r.json()['result'] == 1
        return r

