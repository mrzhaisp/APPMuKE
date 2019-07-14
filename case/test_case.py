#! /usr/bin/env python
#coding=utf-8
#author=zgd
import unittest
import threading
import HTMLTestRunnerChinese
import io
iost = io.StringIO()

class CaseTest(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass
    #跳过用例
    @unittest.skip("CaseTest")
    def test_001(self):
        self.assertEqual(1,1)

    def test_002(self):
        self.assertEqual(2+1,3)

def get_suit(self):
    suit = unittest.TestSuite()
    suit.addTest(CaseTest("test_001"))
    suit.addTest(CaseTest("test_002"))
    htmlfile = "../reporter/report.html"
    fp =  file(htmlfile,"wb")
    HTMLTestRunnerChinese.HTMLTestRunner(f).run(suit)
if __name__ == '__main__':
    # unittest.main()
    threads = []
    for i in range(3):
        t = threading.Thread(target=get_suit)
        threads.append(t)
    for j in threads:
        j.start()













