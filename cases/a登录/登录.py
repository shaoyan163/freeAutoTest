# coding=utf-8 
"""
@Time    : 2019/05/29  上午 9:29 
@Author  : hzsyy
@FileName: test_登录.py
@IDE     : PyCharm
"""

from ddt import ddt, data
import unittest
import json
from common.check import Check
from common.readConfig import confParam
from common.operToken import write_file
from common.readYaml import operYaml
from getRootPath import root_dir
from common.writeLog import writeLog
import os
from common.send import sendRequest


@ddt
class test_登录(unittest.TestCase):
    yaml_path = os.path.join(root_dir, "yamlCase", "登录", "登录1.yaml")
    oper_yaml = operYaml(yaml_path)
    case_list = oper_yaml.caseList()

    method = case_list[0]["method"]
    uri = case_list[1]["uri"]


    # 跳过说明
    reason = confParam("skip_reason")

    @classmethod
    def setUpClass(cls):

        # 声明dict变量存储token
        cls.token_dict = {}

        # 拼接接口地址
        cls.url = confParam("hostName") + cls.uri
        cls.client = sendRequest()

        # 请求信息头
        cls.headers = {"Content-Type": "application/json;charset=UTF-8"}

    # case_list传进去做数据驱动
    @data(*case_list[2:])
    def test_登录(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            email = caseInfo["account"]
            passwd = caseInfo["password"]
            check = caseInfo["assert"]
            self.__dict__['_testMethodDoc'] = caseName

        # 拼装请求参数
        loginData = {"account": email, "userPwd": passwd}

        # 发送请求
        response = self.client.sendRequest(self.method, self.url, self.headers, loginData)

        # 接口返回文本信息
        text = response.text

        # 把文本信息转化为字典格式
        text_dict = json.loads(text)

        # 判断接口响应code是否为200，获取cookie
        if text_dict["code"] == 200:
            self.token_dict["cookie"] = response.headers['Set-Cookie'].split(";")[0]

        # 写日志
        writeLog(caseName, self.url, loginData, check, text_dict)

        # 断言
        Check().check(check, text_dict)


    @classmethod
    def tearDownClass(cls):

        # 把cookie写入文件
        write_file(json.dumps(cls.token_dict))


if __name__ == "__main__":
    unittest.main()
