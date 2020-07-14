
import unittest
class Testcalculator(unittest.TestCase):
    a=int(input('enter value of a:'))
    b=int(input('enter value of b :'))

    @unittest.skip("skip unconditionally")
    def test_add(self):
        c=self.a+self.b
        print('sum of a and b is :',c)

    @unittest.skipIf(b!=0,"b is not 0")
    def test_sub(self):
        print('Difference of a and b is :',self.a-self.b)

    @unittest.skipUnless(a==5,"a is not 5")
    def test_mul(self):
        print('Product of a and b is : ',self.a*self.b)

    @unittest.expectedFailure
    def test_div(self):
        print('quotient of a and b : ',self.c//self.b)

if __name__=="__main__":
    unittest.main(verbosity=2)
