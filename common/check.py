# encoding: utf-8

"""
@author: shaoyanyan
@file: check.py
@time: 2020/2/19 19:12
@ide: pycharm

"""
import json
import unittest

class Check(unittest.TestCase):
    def check(self, hope, text):
        if isinstance(hope, dict):

            for key in hope.keys():
                if isinstance(hope[key], list):
                    for v in hope[key]:
                        self.assertIn(v, text[key])
                else:
                    self.assertEqual(hope[key], text[key])
        elif isinstance(hope, str):
            self.assertIn(hope, str(text))