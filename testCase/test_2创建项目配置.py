# coding=utf-8 
"""
@Time    : 2019/05/25  上午 12:50
@Author  : hzsyy
@FileName: test_创建项目配置.py
@IDE     : PyCharm
"""
import ddt
import unittest
import json
import requests
from common import readConfig
from common.oper_token import read_token


@ddt.ddt
class test_创建项目配置(unittest.TestCase):

    def setUp(self):
        self.url = readConfig.hostName + "/api/assets/v2/project-config"
        self.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization": read_token()["assertToken"]}

    # 把yaml文件参数传进去做数据驱动
    @ddt.file_data("../yaml/创建项目配置.yaml")
    def test_续借(self, **value):

        config_dict = {"projectName": readConfig.projectName}
        data = value["data"]

        for key in data.keys():
            if data[key] in list(config_dict.keys()):
                data[key] = config_dict[data[key]]

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


