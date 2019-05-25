# coding=utf-8 
"""
@Time    : 2019/05/25  上午 9:34 
@Author  : hzsyy
@FileName: readConfig.py
@IDE     : PyCharm
"""
import configparser
from getRootPath import root_dir

config_path = root_dir + "\conf\config.ini"  # 获取配置文件路径
cf = configparser.ConfigParser()

flag = "Test"  # Test、Dev

cf.read(config_path, encoding="utf-8")
secs = cf.sections()

options = cf.options(flag)  # 获取某个section名下所对应的键

hostName = cf.get(flag, "hostName")  # 获取配置文件中对应的值
loginUrl = cf.get(flag, "loginUrl")
appId = cf.get(flag, "appId")
host = cf.get(flag, "host")
user = cf.get(flag, "user")
password = cf.get(flag, "password")
db = cf.get(flag, "db")
riskStrategy = cf.get(flag, "riskStrategy")
riskStrategyName = cf.get(flag, "riskStrategyName")
riskStrategyVersion = cf.get(flag, "riskStrategyVersion")
riskStrategyVersionName = cf.get(flag, "riskStrategyVersionName")
projectName = cf.get(flag, "projectName")


if __name__ == "__main__":
	print(options)
	print(flag)
	print(projectName)




