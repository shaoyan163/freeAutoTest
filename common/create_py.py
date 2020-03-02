# encoding: utf-8

"""
@author: shaoyanyan
@file: create_py.py
@time: 2020/2/20 10:43
@ide: pycharm

"""

import os
import re
import glob

from common import setting


def create_py(yamlDir="", whichYaml=None, pyPath=""):
    # 读取CASE_TEMPLATE文件
    with open(setting.CASE_TEMPLATE, encoding='utf-8') as fr:
        src_content = fr.read()
    dire = yamlDir.split("\\")
    if len(yamlDir.split("\\")) > 1:
        yamlDir, secondDir = yamlDir.split("\\")
        yamlPath = os.path.join(setting.DATA_PATH, yamlDir, secondDir)
    else:
        yamlPath = os.path.join(setting.DATA_PATH, yamlDir)

    all_file = glob.glob(yamlPath + os.sep + '*.yaml')

    if whichYaml:
        all_file = [all_file[whichYaml-1]]
    else:
        all_file = all_file

    for file in all_file:
        fileName = file.split(os.sep)[-1]

        # 获取用例名称，并将名称的首字母大写
        class_name = os.path.split(file)[-1].replace('.yaml', '').capitalize()

        name = class_name.split("_")[0]
        name = re.split("\d", name)[-1]

        # case_template中3个s%的取值
        dire.append(fileName)
        py_content = src_content % (name, str(dire), name)
        casePath = os.path.join(setting.CASE_PATH, pyPath)

        # case目录下创建python文件
        py_path = os.path.join(casePath, "test_" + class_name.lower() + '.py')

        # 向case目录下的python文件中写入内容
        open(py_path, 'w', encoding='utf-8').write(py_content)

        print("yaml文件>>>>>>>>>>>>>>>>>>>%s" % file)
        print("生成的py文件>>>>>>>>>>>>>>>>>>>%s" % py_path)


if __name__ == "__main__":
    yamlPath = "登录"  # yamlCase下面模块路径，为空表示选择的yaml文件yamlCase根目录下*.yaml文件
    whichYaml = None  # None yamlPath 目录下所有的yaml文件都生成py,1表示目录下第一个文件
    pyPath = ""        # case下面模块路径,为空表示生成py文件放在case根目录
    create_py(yamlPath, whichYaml, pyPath)




