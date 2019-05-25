# coding=utf-8 
"""
@Time    : 2019/05/25  下午 12:06 
@Author  : hzsyy
@FileName: readToken.py
@IDE     : PyCharm
"""
from getRootPath import root_dir

token_file = root_dir + r"\conf\tokens"


def write_file(token):
	with open(token_file, "w") as fp:
		fp.write(token)


def read_token():
	with open(token_file) as fp:
		return eval((fp.readlines()[0]))


if __name__ == "__main__":
	token = "12345"
	write_file(token)
	print(read_token()["assertToken"])
	print(read_token()["centerToken"])
	print(read_token()["fundToken"])
