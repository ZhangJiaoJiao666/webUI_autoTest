import os
import unittest
import HTMLTestRunner
from unittest_demo.test_sort import SortTestCase
from unittest_demo.test_abs import AbsTestCase

#设置报告文件保存路径
new_path=os.path.dirname(os.path.realpath(__file__)) #E:\UI_auto_test\unittest_demo\report
# new_path=os.path.dirname(__file__)    #E:/UI_auto_test/unittest_demo\report
report_path=os.path.join(new_path,"report") #将目录名和文件的基名拼接成一个完整的路径
if not os.path.exists(report_path):  #os.path.exists()判断问价是否存在
    os.makedirs(report_path)

suitte=unittest.TestSuite()
suitte.addTest(unittest.makeSuite(AbsTestCase))
suitte.addTest(unittest.makeSuite(SortTestCase))

if __name__=="__main__":
    html_report=report_path + r"\result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="测试报告", description="测试情况描述")
    runner.run(suitte)
