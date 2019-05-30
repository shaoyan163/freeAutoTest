# coding=utf-8 
"""
@Time    : 2019/05/25  上午 10:15 
@Author  : hzsyy
@FileName: test_对外续借接口.py
@IDE     : PyCharm
"""
import os
import random
import string
import time
import ddt
import unittest
from common import readConfig
from common.reNew import renewLoan
from common.readYaml import operYaml
from getRootPath import root_dir
from common.logger import Log


@ddt.ddt
class test_续借(unittest.TestCase):
    yaml_path = os.path.join(root_dir, "yaml", "续借.yaml")
    oper_yaml = operYaml(yaml_path)
    case_list = oper_yaml.caseList()

    # 跳过说明
    reason = readConfig.skip_reason

    @classmethod
    def setUpClass(cls):

        # log 实例化
        cls.log = Log()

    # case_list传进去做数据驱动
    @ddt.data(*case_list)
    def test_续借(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            caseData = caseInfo["data"]
            check = caseInfo["assert"]
            self.__dict__['_testMethodDoc'] = caseName

        time.sleep(1)
        contract_dict = {"personContract": "1558514809015",
                         "successContract": "LX201904030003",
                         "directWithCollect": "LX2019005150011",
                         "enterPriseContract": "T1555989468",
                         "contract": "R" + str(time.time()).split(".")[1] + "".join(random.sample(string.digits, 3)),
                         "collectAccount": "6217002280007862436",
                         "orderId": str(time.time()).replace(".", "1") + "".join(random.sample(string.digits, 3)),
                         }
        data = caseData
        for key in data.keys():
            if data[key] in list(contract_dict.keys()):
                data[key] = contract_dict[data[key]]

        # 发送请求
        text = eval(renewLoan(data))

        # 获取接口返回msg信息
        self.text = text["msg"]

        self.log.info("#" * 100 + "开始测试" + "#" * 100)
        self.log.info("用例名字：{}".format(caseName))
        self.log.info("请求参数：{}".format(data))
        self.log.info("-" * 200)
        self.log.info("期望结果：{}, 实际结果：{}".format(check, text))
        self.log.info("#" * 100 + "测试结束" + "#" * 100)

        # 断言
        self.assertIn(check, self.text)

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == "__main__":
    unittest.main()
