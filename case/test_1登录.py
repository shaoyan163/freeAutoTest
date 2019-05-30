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
import requests
from common import readConfig
from common.operToken import write_file
from common.readYaml import operYaml
from getRootPath import root_dir
from common.logger import Log
import os


@ddt
class test_登录(unittest.TestCase):
    yaml_path = os.path.join(root_dir, "yaml", "登录.yaml")
    oper_yaml = operYaml(yaml_path)
    case_list = oper_yaml.caseList()

    # 跳过说明
    reason = readConfig.skip_reason

    @classmethod
    def setUpClass(cls):

        # log实例化
        cls.log = Log()

        # 声明dict变量存储token
        cls.token_dict = {}

        # 拼接接口地址
        cls.url = readConfig.loginUrl + "/gateway/foundation-user/login/email"

        # 请求信息头
        cls.headers = {"Content-Type": "application/json;charset=UTF-8"}

    # case_list传进去做数据驱动
    @data(*case_list)
    def test_登录(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            email = caseInfo["email"]
            passwd = caseInfo["password"]
            check = caseInfo["assert"]
            self.__dict__['_testMethodDoc'] = caseName
            if "token" in caseInfo.keys():
                token = caseInfo["token"]

        # 拼装请求参数
        loginData = {"email": email, "password": passwd, "appId": readConfig.appId}

        # 发送请求
        response = requests.post(self.url, headers=self.headers, data=json.dumps(loginData))

        # 接口返回文本信息
        text = response.text

        # 把文本信息转化为字典格式
        text_dict = json.loads(text)

        # 判断接口响应code是否为200，获取token
        if text_dict["code"] == str(200):
            self.token_dict[token] = text_dict["body"]["token"]

        self.log.info("#"*100 + "开始测试" + "#"*100)
        self.log.info("用例名字：{}".format(caseName))
        self.log.info("请求参数：{}".format(loginData))
        self.log.info("-" * 200)
        self.log.info("期望结果：{}, 实际结果：{}".format(check, text))
        self.log.info("#"*100 + "测试结束" + "#"*100)

        # 断言
        self.assertIn(check, text)

    @classmethod
    def tearDownClass(cls):

        # 把token写入文件
        write_file(json.dumps(cls.token_dict))


if __name__ == "__main__":
    unittest.main()
