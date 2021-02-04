import json
import os

import pytest
import yaml

absolute_path = os.path.join(os.path.dirname(__file__), 'datas/list_dict_test.yml')
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), 'datas/list_dict_test.yml')))
# print(absolute_path)


def yaml_test():
    # 使用相对路径读取文件，一旦有其他目录下的方法调用这个方法，就没法获取到这个文件了
    # with open("./datas/list_dict_test.yml", encoding='utf-8') as f:
    #     data = yaml.safe_load(f)

    # 所以一般使用绝对路径读取文件
    with open(absolute_path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    test_cases = data
    # print(type(data))
    # # print(data)
    # raw_data = json.dumps(data)
    # print(raw_data)
    # print(type(raw_data))
    return test_cases

class TestParametrizeLearn():
    # @pytest.mark.parametrize(['name', 'pwd'], [("yy1", "123"), ("yy2", "123")])
    # def test_caseget(self, name, pwd):
    #     print(f"姓名是{name}, 密码是{pwd}")

    @pytest.mark.parametrize('get_testcases', [yaml_test()["test_cases"]], indirect=True)
    def test_caseget(self, get_testcases):
        data = get_testcases
        print(data['brokerid'])
        print(data)



# if __name__ == '__main__':
#     test = TestParametrizeLearn()
#     test.yaml_test()