# coding=utf-8 
"""
@Time    : 2019/05/25  上午 12:50
@Author  : hzsyy
@FileName: test_创建项目配置.py
@IDE     : PyCharm
"""
import os
import time

import ddt
import unittest
import json
import requests
from common.readConfig import confParam
from common.operToken import read_token
from common.readYaml import operYaml
from getRootPath import root_dir
from common.logger import Log
from common.findReplace import findAndReplace


@ddt.ddt
class test_创建项目配置(unittest.TestCase):
    yaml_path = os.path.join(root_dir, "yamlCase", "创建项目配置.yaml")
    oper_yaml = operYaml(yaml_path)
    case_list = oper_yaml.caseList()

    # 跳过说明
    reason = confParam("skip_reason")

    @classmethod
    def setUpClass(cls):

        # log 实例化
        cls.log = Log()

        cls.url = confParam("hostName") + "/api/assets/v2/project-config"
        cls.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization": read_token()["assertToken"]}

    # case_list传进去做数据驱动
    @ddt.data(*case_list)
    def test_创建项目配置(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            caseData = caseInfo["data"]
            check = caseInfo["assert"]
            self.__dict__['_testMethodDoc'] = caseName

        config_dict = {"projectName": confParam("projectName")}

        #  用例中值替换为变量
        data = eval(findAndReplace(str(caseData), config_dict))

        # 发送请求
        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        text = response.text  # 接口返回信息

        self.log.info("#" * 100 + "开始测试" + "#" * 100)
        self.log.info("用例名字：{}".format(caseName))
        self.log.info("请求参数：{}".format(data))
        self.log.info("-" * 200)
        self.log.info("期望结果：{}, 实际结果：{}".format(check, text))
        self.log.info("#" * 100 + "测试结束" + "#" * 100)

        # 断言
        self.assertIn(check, text)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()


