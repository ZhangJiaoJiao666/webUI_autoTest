from unittest_demo.test_abs import AbsTestCase
from unittest_demo.test_sort import SortTestCase
import unittest

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(SortTestCase))
suite.addTest(unittest.makeSuite(AbsTestCase))

if __name__=="__main__":
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)