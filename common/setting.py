# encoding: utf-8

"""
@author: shaoyanyan
@file: setting.py.py
@time: 2020/2/20 10:41
@ide: pycharm

"""

import os
from getRootPath import root_dir

# 这个程序主目录
BASE_PATH = root_dir

# 存放yaml文件的路径
DATA_PATH = os.path.join(BASE_PATH, 'yamlCase')

# 测试用例的目录
CASE_PATH = os.path.join(BASE_PATH, 'cases')

# 日志的路径
LOG_PATH = os.path.join(BASE_PATH, 'logs')

# 报告的路径
REPORT_PATH = os.path.join(BASE_PATH, 'report')

# 模板的路径
CASE_TEMPLATE = os.path.join(BASE_PATH, 'conf', 'case_template')


if __name__ == "__main__":
    print(CASE_PATH)