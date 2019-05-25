# coding=utf-8 
"""
@Time    : 2019/05/24  下午 12:36 
@Author  : hzsyy
@FileName: sendEmail.py
@IDE     : PyCharm
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

username = 'xxxxxxxxx'
password = "xxxxxxxxx"
sender = username
receivers = ','.join(['xxxxxxxxxx'])


def email(report):
	# 设置请求头信息
	msg = MIMEMultipart()
	msg['Subject'] = '接口测试报告'  # 邮件名
	msg['From'] = sender
	msg['To'] = receivers

	jpgpart = MIMEApplication(open(report, 'rb').read())
	jpgpart.add_header('Content-Disposition', 'attachment', filename='接口测试报告.html')
	msg.attach(jpgpart)

	#发送邮件
	client = smtplib.SMTP()
	client.connect('smtp.163.com')
	client.login(username, password)
	client.sendmail(sender, receivers, msg.as_string())
	client.quit()
	print("邮件发送成功，请查看")