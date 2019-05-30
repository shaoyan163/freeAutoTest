# coding=utf-8 
"""
@Time    : 2019/05/22  下午 2:26 
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
# orgId = "279019574023296265"
# priKey = "MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAI6O2ctV0hlV4w9n2mghgAY1YFgi5coMG0P+pxq8kFjgd+P4qBNtX2x599hh48f5MXqYHMPhky5oCODp2mwcVAfQOg7Yh4qdj4RXVR9TYfy+MCp65W4th5QTcZMnosI7qwGrOlSEgcTLH7KD5u9Q3yBnZgtV9gVcLiwf0uzojfW9AgMBAAECgYBMf5uf4Y28yrntqm0pM9DfhAUPRqrIoXaAJkbFsipDhzDOxMBsrGRocYruMplo1fAXOUk2U/YHEQyypMrw+MKeG2hpElCIzrDe9yzGB+evE/soWEHAbnAOkCD9yOnnS3pd2lcKQGFXDXYys4tlTZ2zh67bNBB/QXk2s1rkjn/SgQJBAPStAt783V+jNJKiw1IAlf8lN2Ublz1mpXqz8UKDRgyl9kSAc8zJZfs8GdTSl70Jnvp8CbW1htv/8Gbays5JG08CQQCVJ+srNEq23U3YpN6InkOaoTjTU8rwtRpjSNQjQwG8Ky25u7U4c3uWuPem8MEmVK6TkIlofoxYosKAs/DiVOszAkBBeP54rw+J5QFPb9B2ZAO/V7UgECcDXjFPyVD47GnVPp/MqtbR6N6qQOXkpknGYwmwm3p5rk6dFjq9OzTjyHpPAkBC7EdC+lJvm/oas1a5m7Efhyj1AMq0l72AQKQWMjFsGT+J72PPMVmJdfKAL9Op/CLcSOSuQuF7v4Nftdzl4E4rAkEA7R53VGnR1magryj8rC0QY1Lzar2JIcpKGLzcDnh8jI94iOQPd9LpirNHbAQSRA4RBCQ90h0Yfxp1N5fu5pgJUA=="
# pubKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCOjtnLVdIZVeMPZ9poIYAGNWBYIuXKDBtD/qcavJBY4Hfj+KgTbV9seffYYePH+TF6mBzD4ZMuaAjg6dpsHFQH0DoO2IeKnY+EV1UfU2H8vjAqeuVuLYeUE3GTJ6LCO6sBqzpUhIHEyx+yg+bvUN8gZ2YLVfYFXC4sH9Ls6I31vQIDAQAB"
# print("机构ID: ", orgId)
# print("private_key: ", priKey)
# print("public_key: ", pubKey)
infoDict = {"orgId": orgId, "pubKey": pubKey, "priKey": priKey}


def getEncry(data):
	header = {"Content-Type": "application/json;charset=UTF-8", "Accept": "text/plain"}
	encodeInfo = parse.urlencode(infoDict)

	url = "http://10.200.154.11:8082/v2/sys/admin?%s" % encodeInfo
	response = requests.post(url, headers=header, data=json.dumps(data))
	# print("*" * 50 + "加密前数据为" + "*" * 50)
	# print(data)
	# print("*"*50 + "加密后数据为" + "*"*50)
	# print(response.text)
	# print("#" * 50)
	return response.text


def renewLoan(data):
	header = {"Content-Type": "application/json"}
	if environment == "test":
		url = "http://test-ats.fengdai.org/api/ats/v2/loan-application-manage/_renewal"  # 测试环境续借地址
	elif environment == "dev":
		url = "http://atsdev.fengdai.org/api/ats/v2/loan-application-manage/_renewal"  # 开发环境续借地址
	elif environment == "uat":
		url = "https://uat-ats.trc.com/api/ats/v2/loan-application-manage/_renewal"  # 预发环境续借地址
	else:
		url = "https://ats.trc.com/api/ats/v2/loan-application-manage/_renewal"  # 生产环境续借地址
	application = getEncry(data)

	response = requests.post(url, headers=header, data=application)
	return response.text


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
