import pytest
import pytest_dependency
class Testcalculator:
    a=int(input('enter value of a:'))
    b=int(input('enter value of b :'))
    #pytestmark=pytest.mark.skip(reason="skip entire module")
    #@pytest.mark.skip
    def test_add(self):
        c=self.a+self.b
        print('sum of a and b is :',c)

    @pytest.mark.skipif(a==10,reason='skip')
    def test_sub(self):
        print('Difference of a and b is :',self.a-self.b)

    @pytest.mark.dependency(name='a')
    @pytest.mark.parametrize('arg1,arg2',[(10,5)])
    def test_mul(self,arg1,arg2):
        print(arg1)
        print(arg3)
        print('Product of a and b is : ',arg1*arg2)

    def test_div(self):
        print('quotient of a and b : ',self.a//self.b)

    #@pytest.mark.dependency(depends=['a'])
    @pytest.mark.parametrize('args',[1,2,3])
    def test_add1(self,args):
        print(1+args)

    def test_assert(self):
        assert 10==1,'hello'
        print('hiai')




