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
from common.logger import Log


@ddt.ddt
class test_登录(unittest.TestCase):
    # 实例化Log
    log = Log()

    # 声明dict变量存储token
    token_dict = {}

    def setUp(self):
        # 拼接接口地址
        self.url = readConfig.loginUrl + "/gateway/foundation-user/login/email"

        # 请求信息头
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}

    # 把yaml文件参数读进来
    @ddt.file_data("../yaml/登录.yaml")
    def test_续借(self, **value):

        self.log.info("开始测试" + "#"*200)

        # 拼装请求参数
        loginData = {"email": value["email"], "password": value["password"], "appId": readConfig.appId}

        self.log.info("请求参数:{}".format(loginData))

        # 发送请求
        response = requests.post(self.url, headers=self.headers, data=json.dumps(loginData))

        # 接口返回文本信息
        text = response.text

        # 把文本信息转化为字典格式
        text_dict = json.loads(text)

        # 判断接口响应code是否为200，获取token
        if text_dict["code"] == str(200):
            self.token_dict[value["token"]] = text_dict["body"]["token"]
            write_file(json.dumps(self.token_dict))

        print("#"*200)
        print("请求参数：", loginData)
        print("+"*200)
        print("期望结果：{}, 实际结果：{}".format(value["assert"], text))
        print("#" * 200)

        # 打印日志到log文件
        self.log.info("期望结果：{}".format(value["assert"]))
        self.log.info("实际结果：{}".format(text))
        self.log.info("测试结束" + "#"*200)

        # 断言
        self.assertIn(value["assert"], text)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
