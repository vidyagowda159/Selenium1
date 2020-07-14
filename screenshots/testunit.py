import unittest

class Testex(unittest.TestCase):

    def setUp(self):
        print('in setup method')

    def tearDown(self):
        print('in tear down method')

    def test_func1(self):
        print('in func1')

    def test_func2(self):
        print('in func2')

if __name__ =='__main__':
    unittest.main()