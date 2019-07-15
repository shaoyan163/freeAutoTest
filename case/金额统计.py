# coding=utf-8 
"""
@Time    : 2019/06/03  下午 3:32 
@Author  : hzsyy
@FileName: test_5借款申请统计.py
@IDE     : PyCharm
"""

import os

import ddt
import unittest
import json
import requests
from common.readConfig import confParam
from common.readYaml import operYaml
from getRootPath import root_dir
from common.logger import Log
from common.dataBase import dataBase

@ddt.ddt
class test_借款申请统计(unittest.TestCase):
    yaml_path = os.path.join(root_dir, "yaml", "借款申请统计.yaml")
    oper_yaml = operYaml(yaml_path)
    case_list = oper_yaml.caseList()

    # 跳过说明
    reason = confParam("skip_reason")

    @classmethod
    def setUpClass(cls):

        # log 实例化
        cls.log = Log()

        # 数据库实例化
        cls.db = dataBase()

    # case_list传进去做数据驱动
    @ddt.data(*case_list)
    @unittest.skip(reason)
    def test_借款申请统计(self, cases):

        for caseName, caseInfo in cases.items():
            caseName = caseName
            current_page_sql = caseInfo["current_page"]
            total_amount_sql = caseInfo["total_amount"]
            self.__dict__['_testMethodDoc'] = caseName

        # 数据库执行sql
        currPageSumAmount = self.db.getSumAmount(current_page_sql)
        totalSumAmount = self.db.getSumAmount(total_amount_sql)

        self.log.info("#" * 100)
        self.log.info("{}为：{}".format(caseName, currPageSumAmount))
        self.log.info("{},当前条件总金额为：{}".format(caseName, totalSumAmount))
        self.log.info("+" * 100)

    @classmethod
    def tearDownClass(cls):
        cls.db.closeDb()


if __name__ == "__main__":
    unittest.main()

