# coding=utf-8 
"""
@Time    : 2018/05/26  上午 11:14
@Author  : hzsyy
@FileName: getRootPath.py
@IDE     : PyCharm
"""
import os

root_dir = os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":
    print(root_dir)
    yaml_path = os.path.join(root_dir, "yamlCase", "登录", "登录.yaml")
    print(yaml_path)