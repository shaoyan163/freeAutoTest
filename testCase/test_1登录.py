# coding=utf-8 
"""
@Time    : 2019/05/25  上午 10:50
@Author  : hzsyy
@FileName: test_登录.py
@IDE     : PyCharm
"""
import ddt
import unittest
import json
import requests
from common import readConfig
from common.oper_token import write_file


@ddt.ddt
class test_登录(unittest.TestCase):
    token_dict = {}

    def setUp(self):
        self.url = readConfig.loginUrl + "/gateway/foundation-user/login/email"
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}

    # 把yaml文件参数传进去做数据驱动
    @ddt.file_data("../yaml/登录.yaml")
    def test_续借(self, **value):
        loginData = {"email": value["email"], "password": value["password"], "appId": readConfig.appId}

        # 发送请求
        response = requests.post(self.url, headers=self.headers, data=json.dumps(loginData))
        text = response.text  # 接口返回信息

        text_dict = json.loads(text)
        if text_dict["code"] == str(200):
            test_登录.token_dict[value["token"]] = text_dict["body"]["token"]
            write_file(json.dumps(test_登录.token_dict))

        print("#"*200)
        print("请求参数：", loginData)
        print("+"*200)
        print("期望结果：{}, 实际结果：{}".format(value["assert"], text))
        print("#" * 200)

        # 断言
        self.assertIn(value["assert"], text)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
