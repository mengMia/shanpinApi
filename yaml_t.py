from learning_pytest import parametrize_test
from learning_pytest.parametrize_test import TestParametrizeLearn

t = TestParametrizeLearn()
def yam_t():
    data = t.yaml_test()
    print(data)
if __name__ == '__main__':
    yam_t()