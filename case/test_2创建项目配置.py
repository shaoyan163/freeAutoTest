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
from common.operToken import read_token
from common.readYaml import operYaml
from getRootPath import root_dir

reason = readConfig.skip_reason


@ddt.ddt
class test_创建项目配置(unittest.TestCase):
    yaml_path = root_dir + "\\yaml\\创建项目配置.yaml"
    oper_yaml = operYaml(yaml_path)
    case_list = oper_yaml.caseList()

    @classmethod
    def setUpClass(cls):
        cls.url = readConfig.hostName + "/api/assets/v2/project-config"
        cls.headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization": read_token()["assertToken"]}

    # case_list传进去做数据驱动
    @ddt.data(*case_list)
    def test_创建项目配置(self, cases):
        self.__dict__['_testMethodDoc'] = ([caseName for caseName in cases.keys()][0])

        for caseName, caseInfo in cases.items():
            caseName = caseName
            caseData = caseInfo["data"]
            check = caseInfo["assert"]

        config_dict = {"projectName": readConfig.projectName}
        data = caseData
        for key in data.keys():
            if data[key] in list(config_dict.keys()):
                data[key] = config_dict[data[key]]

        # 发送请求
        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        text = response.text  # 接口返回信息

        print("#"*200)
        print("用例名字：{}".format(caseName))
        print("请求参数：", data)
        print("+"*200)
        print("期望结果：{}, 实际结果：{}".format(check, text))
        print("#" * 200)

        # 断言
        self.assertIn(check, text)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()


