import os

import yaml


class ReadFile():
    def __init__(self):
        # os.path.dirname(__file__) 获取当前脚本运行的绝对路径
        # D: / CS / PythonCode / common
        # os.path.dirname(os.path.dirname(__file__))去掉当前脚本运行的绝对路径的最后一个路径，
        # D:/CS/PythonCode

        # 拼接为绝对路径，还有点问题
        # 拼接的路径结果是：D:/CS/PythonCode\config/test.yaml，但是yaml读取这个路径的时候没报错
        self.test_yaml_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config/test.yaml')
        self.redis_yaml_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config/redisKey.yaml')

    def read_yaml(self, path_type):
        file_path = ''
        if path_type == 'test_yaml_path':
            file_path = self.test_yaml_path
        elif path_type == 'redis_yaml_path':
            file_path = self.redis_yaml_path

        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f.read())
            return data

    def read_excel(self):
        # todo:读取excel文件
        pass

if __name__ == '__main__':
    test = ReadFile()
    test.read_yaml('test_yaml_path')