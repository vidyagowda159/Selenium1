import pytest
class TestCacli():

    @pytest.fixture(autouse=True)
    def inputValue(self):
        a=int(input('enter value of a : '))
        b= int(input('enter value of b : '))

    def test_add(self,inputValue):
        print("adding a and b")

    def test_sub(self):
        print("subtracting a and b", self.a - self.b)

    def test_mul(self):
        print("multiplying a and b",self.a*self.b)

    def test_div(self,):
        print("dividing a and b", self.a / self.b)






