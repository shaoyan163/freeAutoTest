# coding=utf-8 
"""
@Time    : 2019/05/25  上午 13:50
@Author  : hzsyy
@FileName: test_审核项目配置.py
@IDE     : PyCharm
"""
import os

import ddt
import unittest
import json
import requests

from common.findReplace import findAndReplace
from common.readConfig import confParam
from common.dataBase import dataBase
from common.operToken import read_token
from common.readYaml import operYaml
from getRootPath import root_dir
from common.logger import Log


@ddt.ddt
class test_审核项目配置(unittest.TestCase):
    yaml_path = os.path.join(root_dir, "yaml", "审核拒绝项目配置.yaml")
    oper_yaml = operYaml(yaml_path)
    case_list = oper_yaml.caseList()

    # 跳过说明
    reason = confParam("skip_reason")

    @classmethod
    def setUpClass(cls):

        # log 实例化
        cls.log = Log()

        # 获取创建项目名字
        projectName = "审核拒绝项目测试"
        url = confParam("hostName") + "/api/assets/v2/project-config"
        cls.asset_headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization": read_token()["assertToken"]}
        data = {"assetKind": "CREDIT", "projectName": projectName, "projectType": "PRO_CONSUMPTION"}
        response = requests.post(url, headers=cls.asset_headers, data=json.dumps(data))

        # 数据库实例化
        db = dataBase()

        cls.config_number = db.configId("id", "loan_project_config", "project_name", projectName)
        cls.url = confParam("hostName") + "/api/center/v2/project-config/_audit-failure"
        cls.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization": read_token()["centerToken"]}

    # case_list传进去做数据驱动
    @ddt.data(*case_list)
    def test_审核拒绝项目配置(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            caseData = caseInfo["data"]
            check = caseInfo["assert"]
            self.__dict__['_testMethodDoc'] = caseName

        ids = {"id": self.config_number}

        #  用例中值替换为变量
        data = eval(findAndReplace(str(caseData), ids))

        # 发送请求
        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))

        # 接口返回信息
        text = response.text

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
        # 删除项目配置
        url = confParam("hostName") + "/api/assets/v2/project-config/%s" % cls.config_number
        response = requests.delete(url, headers=cls.asset_headers)


if __name__ == "__main__":
    unittest.main()
