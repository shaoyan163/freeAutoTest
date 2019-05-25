# coding=utf-8 
"""
@Time    : 2019/05/24  下午 12:42 
@Author  : hzsyy
@FileName: run1.py
@IDE     : PyCharm
"""
import time
import unittest
from BeautifulReport import BeautifulReport
from common import sendEmail
from getRootPath import root_dir

test_dir = root_dir + "\\testCase"
reportPath = root_dir + "\\testReport"
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

now = time.strftime("%Y-%m-%d %H_%M_%S")
reportName = now + '测试报告.html'
description = "ATS系统接口自动化测试报告"
BeautifulReport(discover).report(filename=reportName, description=description, report_dir=reportPath)
report = reportPath + "\\" + reportName

# 发送邮件
# sendEmail.email(report)
