import unittest
from unittest_Pack.testCases import testFixtures
from unittest_Pack.testCases import testSkip
t1 = unittest.TestLoader().loadTestsFromTestCase(testFixtures.Testfix)
t2 = unittest.TestLoader().loadTestsFromTestCase(testSkip.Testcalculator)

suiteObj = unittest.TestSuite([t1,t2])
unittest.TextTestRunner().run(suiteObj)

