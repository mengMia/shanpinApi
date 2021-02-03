import os

import pytest
import yaml


class TestParametrizeLearn():
    # def filepath(self):
    absolute_path = os.path.join(os.path.dirname(__file__), 'datas/list_dict_test.yml')
    print(os.path.abspath(os.path.join(os.path.dirname(__file__), 'datas/list_dict_test.yml')))
    print(absolute_path)

    def yaml_test(self):
        # 使用相对路径读取文件，一旦有其他目录下的方法调用这个方法，就没法获取到这个文件了
        # with open("./datas/list_dict_test.yml", encoding='utf-8') as f:
        #     data = yaml.safe_load(f)

        # 所以一般使用绝对路径读取文件
        with open(self.absolute_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        print(type(data))
        print(data)
        return data

if __name__ == '__main__':
    test = TestParametrizeLearn()
    test.yaml_test()