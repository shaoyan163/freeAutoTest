# coding=utf-8 

from ddt import ddt, data
import unittest
import json
from common.check import Check
from common.dataBase import dataBase
from common.findReplace import findAndReplace
from common.readConfig import confParam
from common.operToken import read_token
from common.readYaml import operYaml
from common.writeLog import writeLog
import os
from common.send import sendRequest
from getRootPath import root_dir


@ddt
class test_修改车型(unittest.TestCase):
    yaml_path = os.path.join(root_dir, "yamlCase", "车辆管理", "3修改车型_6383修改车型.yaml")
    oper_yaml = operYaml(yaml_path)
    case_list = oper_yaml.caseList()

    method = case_list[0]["method"]
    uri = case_list[1]["uri"]

    # 跳过说明
    reason = confParam("skip_reason")

    @classmethod
    def setUpClass(cls):

        # 拼接接口地址
        cls.url = confParam("hostName") + cls.uri
        cls.client = sendRequest()

        dbName = confParam("车辆管理")
        db = dataBase(dbName)
        cls.car_model_id = db.getId("car_model_id", "t_info_car_model", "brand_name", "比亚迪OFO")

        # 请求信息头
        cls.headers = {"Cookie": read_token()["cookie"], "Content-Type": "application/json;charset=UTF-8"}

    # case_list传进去做数据驱动
    @data(*case_list[2:])
    def test_修改车型(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            data = caseInfo["data"]
            check = caseInfo["check"]
            self.__dict__['_testMethodDoc'] = caseName

        ids = {"carModelId": self.car_model_id}

        #  用例中值替换为变量
        data = eval(findAndReplace(str(data), ids))

        # 发送请求
        response = self.client.sendRequest(self.method, self.url, self.headers, data)

        # 接口返回文本信息
        text = response.text

        # 把文本信息转化为字典格式
        text_dict = json.loads(text)

        # 写日志
        writeLog(caseName, self.url, data, check, text_dict)

        # 断言
        Check().check(check, text_dict)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()
