# coding=utf-8 
"""
@Time    : 2019/05/25  上午 9:34 
@Author  : hzsyy
@FileName: readConfig.py
@IDE     : PyCharm
"""

import configparser
import os
from getRootPath import root_dir

config_path = os.path.join(root_dir, "conf", "config.ini")  # 获取配置文件路径
cf = configparser.ConfigParser()

flag = "Test"  # Test、Dev


def confParam(name):
	cf.read(config_path, encoding="utf-8")

	# 获取配置文件中所有section
	secs = cf.sections()

	# 获取某个section名下所对应的键
	options = cf.options(flag)

	# 返回配置文件中name所对应的值
	return cf.get(flag, name)


if __name__ == "__main__":
	params = confParam("projectName")
	print(params)





