# coding=utf-8 
"""
@Time    : 2019/05/29  上午 9:29 
@Author  : hzsyy
@FileName: test_登录.py
@IDE     : PyCharm
"""
from ddt import ddt,data,unpack
import unittest
import json
import requests
from common import readConfig
from common.operToken import write_file
from common.readYaml import operYaml
from getRootPath import root_dir
reason = readConfig.skip_reason

@ddt
class test_登录(unittest.TestCase):
    yaml_path = root_dir + "\\yaml\\登录.yaml"
    oper_yaml = operYaml(yaml_path)
    case_list = oper_yaml.caseList()

    @classmethod
    def setUpClass(cls):
        # 声明dict变量存储token
        cls.token_dict = {}

        # 拼接接口地址
        cls.url = readConfig.loginUrl + "/gateway/foundation-user/login/email"

        # 请求信息头
        cls.headers = {"Content-Type": "application/json;charset=UTF-8"}

    # case_list传进去做数据驱动
    @data(*case_list)
    def test_登录(self, cases):
        self.__dict__['_testMethodDoc'] = ([caseName for caseName in cases.keys()][0])

        for caseName, caseInfo in cases.items():
            caseName = caseName
            email = caseInfo["email"]
            passwd = caseInfo["password"]
            check = caseInfo["assert"]
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

        print("#"*200)
        print("用例名字：{}".format(caseName))
        print("请求参数：", loginData)
        print("+"*200)
        print("期望结果：{}, 实际结果：{}".format(check, text))
        print("#" * 200)

        # 断言
        self.assertIn(check, text)

    @classmethod
    def tearDownClass(cls):
	
        # 把token写入文件
        write_file(json.dumps(cls.token_dict))


if __name__ == "__main__":
    unittest.main()
