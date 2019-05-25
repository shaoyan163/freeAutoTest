# coding=utf-8 
"""
@Time    : 2019/05/25  下午 2:51 
@Author  : hzsyy
@FileName: database.py
@IDE     : PyCharm
"""
import pymysql
from common import readConfig


class dataBase:
	def __init__(self):
		self.host = readConfig.host
		self.user = readConfig.user
		self.password = readConfig.password
		self.db = readConfig.db
		self.con = pymysql.connect(host=self.host, user=self.user, password=self.password,
		                           db=self.db, port=3306, charset="utf8")
		self.cur = self.con.cursor()

	def configId(self, col_name, table_name, project_name, key):
		sql = "Select {} from {} where {} ='{}'".format(col_name, table_name,project_name, key)
		self.cur.execute(sql)
		self.cur.close()
		self.con.close()
		return self.cur.fetchall()[0][0]


if __name__ == "__main__":
	db = dataBase()
	config_number = db.configId("id", "loan_project_config", "project_name", "测试专用电商通")
	print(config_number)