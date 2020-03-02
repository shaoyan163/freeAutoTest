# coding=utf-8 
"""
@Time    : 2019/12/24  下午 14:42
@Author  : hzsyy
@FileName: run.py
@IDE     : PyCharm
"""
import time
import unittest
from BeautifulReport import BeautifulReport
from common import sendEmail
from getRootPath import root_dir
import os


def run():
    test_dir = os.path.join(root_dir, "cases")
    reportPath = os.path.join(root_dir, "report")
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    reportName = now + '测试报告.html'
    description = "左中右系统接口自动化测试报告"
    BeautifulReport(discover).report(filename=reportName, description=description, report_dir=reportPath)
    # print(discover)
    report = os.path.join(reportPath, reportName)

    # 发送邮件
    # sendEmail.email(report)


if __name__ == "__main__":
   run()
