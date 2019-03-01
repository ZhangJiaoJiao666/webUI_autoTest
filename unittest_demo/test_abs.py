import unittest
from ddt import ddt,unpack,data
from unittest_demo.abs import abs
@ddt
class AbsTestCase(unittest.TestCase):
    def setUp(self):
        print("test method start......")

    @data([2,1],[-1,1],[0,0])
    @unpack
    def test_abs(self, n, expected_value):
        result = abs(n)
        self.assertEqual(result, expected_value, msg = result)

    def tearDown(self):
        print("test method over......")
if __name__=='__main__':
    unittest.main(verbosity=2)

