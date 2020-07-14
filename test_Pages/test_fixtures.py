import pytest
@pytest.fixture(scope="class",autouse=True,params=["chrome","firefox"])
def setup(request):
    print("\n1")
    print("params are : ", request.param)
    yield
    print("\n2")

class Testfixex():
    def test_f1(self):
        print('f1')

    def test_f2(self):
        print('\nf2')

#@pytest.mark.usefixtures("setup")
class TestEx2():

    def test_f3(self):
        print("\nf3")
