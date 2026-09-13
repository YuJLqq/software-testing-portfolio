# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
from unittest_framework.read_case import *
class do_case01(unittest.TestCase):
    def setUp(self):
        print("测试开始ʼ")
    def test_login(self):
        readCase("login")
    def test_order(self):
        readCase("order")

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(do_case01("test_login"))
    suite.addTest(do_case01("test_order"))
    filename=r"C:\Users\lenovo\Desktop\测试培训\orderweb.html"
    fs = open(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fs,title="这是一份自动化测试报告文件",description="2026-06-16")
    runner.run(suite)
    fs.close()    
    