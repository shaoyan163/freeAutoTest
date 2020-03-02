# coding=utf-8 
"""
@Time    : 2020/02/13  上午 12:50
@Author  : hzsyy
@FileName: 修改密码.py
@IDE     : PyCharm
"""
import os
from ddt import ddt, data
import unittest
from common.check import Check
from common.send import sendRequest
from common.readConfig import confParam
from common.operToken import read_token
from common.readYaml import operYaml
from getRootPath import root_dir
from common.writeLog import writeLog


@ddt
class test_修改密码(unittest.TestCase):
    yaml_path = os.path.join(root_dir, "yamlCase", "登录", "2修改密码_5732修改密码.yaml")
    oper_yaml = operYaml(yaml_path)
    case_list = oper_yaml.caseList()

    method = case_list[0]["method"]
    uri = case_list[1]["uri"]


    # 跳过说明
    reason = confParam("skip_reason")

    @classmethod
    def setUpClass(cls):

        cls.url = confParam("hostName") + cls.uri
        cls.client = sendRequest()
        cls.headers = {"Cookie": read_token()["cookie"], "Content-Type": "application/json;charset=UTF-8"}

    # case_list传进去做数据驱动
    @data(*case_list[2:])
    def test_修改密码(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            data = caseInfo["data"]
            check = caseInfo["check"]
            self.__dict__['_testMethodDoc'] = caseName

        # 发送请求
        response = self.client.sendRequest(self.method, self.url, self.headers, data)

        text = response.text  # 接口返回信息

        # 写日志
        writeLog(caseName, self.url, data, check, text)

        # 断言
        Check().check(check, text)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()


