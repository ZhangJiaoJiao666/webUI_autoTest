import unittest
from unittest_demo.sort import sort
from ddt import ddt,unpack,data

@ddt
class SortTestCase(unittest.TestCase):

    def setUp(self):
        print("开始测试。。。。")

    @data([1,0,2],[1,1,10],[1,2,20],[0,0,0])
    @unpack
    def test_Sort(self,num,type,expected_value):
        result = sort(num,type)
        self.assertEqual(result, expected_value, msg = result)
    def tearDown(self):
        print("结束测试。。。。 ")
if __name__=="__main__":
    unittest.main(verbosity=2)
