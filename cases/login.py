import json
import urllib3
import requests

login_url = "http://115.236.51.227:55890/api/login"


def login():
    data = {"account":"admin", "password": "123456"}
    headers = {"Content-Type": "application/json;charset=UTF-8"}

    response = requests.post(url=login_url, data=json.dumps(data), headers=headers)
    print(response.text)
    cookie = response.headers['Set-Cookie'].split(";")[0]
    print(cookie)
    return cookie


def get_user_info():
    params = {"channelType":"","current":1,"size":10,"userId":"","userNo":"","name":"","telphone":"",
          "authentication":"","area":"","companyId":"","regTime":"","regTimeStart":"","regTimeEnd":"","authTime":"",
          "authTimeStart":"","authTimeEnd":"","workUnit":"","freeDeposit":"","userStatus":"",
          "channelId":"","identity":"","ocrCompare":"","depositPayStartTime":"","depositPayEndTime":""}
    headers = {"Cookie":login()}
    url = "http://115.236.51.227:55890/api/user/list"
    resp = requests.post(url, params=params, headers=headers)
    print(resp.text)


if __name__ == "__main__":
    get_user_info()
