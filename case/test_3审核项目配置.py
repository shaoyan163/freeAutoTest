# coding=utf-8 
"""
@Time    : 2019/05/25  上午 13:50
@Author  : hzsyy
@FileName: test_审核项目配置.py
@IDE     : PyCharm
"""
import ddt
import unittest
import json
import requests
from common import readConfig
from common.dataBase import dataBase
from common.oper_token import read_token


@ddt.ddt
class test_审核项目配置(unittest.TestCase):

    def setUp(self):

        projectName = readConfig.projectName  # 获取创建项目名字
        print(projectName)
        db = dataBase()
        self.config_number = db.configId("id", "loan_project_config", "project_name", projectName)
        self.url = readConfig.hostName + "/api/center/v2/project-config/_audit-success"
        self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization": read_token()["centerToken"]}

    # 把yaml文件参数传进去做数据驱动
    @ddt.file_data("../yaml/审核项目配置.yaml")
    def test_审核项目配置(self, **value):

        ids = {"id": self.config_number,
               "riskStrategy": readConfig.riskStrategy,
               "riskStrategyName": readConfig.riskStrategyName,
               "riskStrategyVersion": readConfig.riskStrategyVersion,
               "riskStrategyVersionName": readConfig.riskStrategyVersionName
               }

        data = value["data"]
        for key in data.keys():
            if data[key] in list(ids.keys()):
                data[key] = ids[data[key]]

        # 发送请求
        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        text = response.text  # 接口返回信息

        print("#"*200)
        print("请求参数：", data)
        print("+"*200)
        print("期望结果：{}, 实际结果：{}".format(value["assert"], text))
        print("#" * 200)

        # 断言
        self.assertIn(value["assert"], text)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
