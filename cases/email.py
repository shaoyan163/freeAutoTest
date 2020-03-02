# -*- coding:UTF-8-*-
# Author: dx
from urllib import request
import json

access_token = "xxx"


def send_msg(mobile, item_name):
    """
     钉钉机器人API接口地址:
     https://oapi.dingtalk.com/robot/send?access_token=6bfc67fbdcdc3e2ea38e11d77a1d1f378188479102fcfcda53686debac0297aa
     :param mobile:
     :param itemName:
     :return:
    """
    url = "https://oapi.dingtalk.com/robot/send?access_token=6bfc67fbdcdc3e2ea38e11d77a1d1f378188479102fcfcda53686debac0297aa"      # 钉钉中webhook的值进行拼接
    data = {
        "msgtype": "text",
        "text": {
            "content": item_name
        },
        "at": {
            "atMobiles": [
                mobile
            ],
            "isAtAll": "false"
        }
    }
    # 设置编码格式
    json_data = json.dumps(data).encode(encoding='utf-8')
    print(json_data)
    header_encoding = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                       "Content-Type": "application/json"}
    req = request.Request(url=url, data=json_data, headers=header_encoding)
    res = request.urlopen(req)
    res = res.read()
    print(res.decode(encoding='utf-8'))


if __name__ == "__main__":
    mobile = "*******"     # 需要艾特的人员钉钉对应的手机号码
    item_name = "test"
    send_msg(mobile, item_name)