# coding=utf-8 
"""
@Time    : 2018/05/22  下午 2:26
@Author  : hzsyy
@FileName: ency.py
@IDE     : PyCharm
"""

import json
import random
import string
import time

import pymysql
import requests
from urllib import parse


dbInfo = {"test": ["10.200.154.23", "atstest", "ats3306TEST", "米今测试"],
          "dev": ["dts-db.fengdai.org", "dts", "dts.666dev", "小蜜蜂开发测试"],
		  # "uat": ["10.200.170.12", "atsuat", "ats3306UAT", "泰链科技技术有限公司"],
        "uat": ["10.200.170.12", "atsuat", "ats3306UAT", "小蜜蜂融资租赁(上海)有限公司"]
          }
env = dbInfo["test"]
host = env[0]
userName = env[1]
environment = "test"  # test 测试环境；dev 开发环境；uat 预发环境； pro生产环境
passwd = env[2]
remark = env[3]


def getData(host, userName, passwd, remark):
	connect = pymysql.connect(host=host, user=userName, password=passwd, db="focus_dts", port=3306, charset="utf8")
	cur = connect.cursor()
	sql = "SELECT  party_org_id,private_key,public_key FROM party_org_key WHERE remark='%s'" % remark
	cur.execute(sql)
	return cur.fetchall()[0]


info = getData(host, userName, passwd, remark)
orgId = info[0]
priKey = info[1]
pubKey = info[2]
infoDict = {"orgId": orgId, "pubKey": pubKey, "priKey": priKey}


def getEncry(data):
	header = {"Content-Type": "application/json;charset=UTF-8", "Accept": "text/plain"}
	encodeInfo = parse.urlencode(infoDict)

	url = "http://10.200.154.11:8082/v2/sys/admin?%s" % encodeInfo
	response = requests.post(url, headers=header, data=json.dumps(data))
	return response.text


def renewLoan(data):
	header = {"Content-Type": "application/json"}
	if environment == "test":
		url = "http://test-ats.fengdai.org/api/ats/v2/loan-application-manage/_renewal"  # 测试环境续借地址


if __name__ == "__main__":
	orderId = str(time.time()).replace(".", "1") + ("").join(random.sample(string.digits, 3))
	data = {"oldContract": "LX2019005160003","contract":"111111","amount":1,"loanTerms":1,
	    "repayRate":0.01,"repayRateType":"YEAR_RATES","orderId": orderId,
	    "attachments":[
		    {"id":1558506832071,
		        "name":"12.jpg",
		        "fileType":"jpg",
		        "fileUrl":"FnxsCx-L0vTFKblRRh086K1ITn1R",
		        "kind":"LOAN_APPLICATION_PROOF_MATERIAL"}]
	    }
	renewLoan(data)
