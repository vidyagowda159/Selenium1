import unittest
def setUpModule():
    print('in setup module')
def tearDownModule():
    print('in teardown module')
class Testfix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("value of cls :")
        print("in setup class")
    @classmethod
    def tearDownClass(cls):
        print('in teardown class')
    def setUp(self):
        print('in setup function')
    def tearDown(self):
        print('in teardown function')
    def testAdd(self):
        print('addition is : ',20+30)
if __name__=="__main__":
    unittest.main(verbosity=2)