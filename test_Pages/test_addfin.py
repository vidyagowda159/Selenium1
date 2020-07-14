import pytest
from selenium.webdriver.common.keys import Keys
from settings import wd,url
class TestFinaliser:

    search_bar = '//input[@name="q"]'

    @pytest.fixture(autouse=True,params=[url[1],url[2]])
    def initialization(self,request):
        print("in init")
        print("data in request : ",request)
        wd.get(url[0])
        wd.maximize_window()

        def finalizer():
            print('in finalizer')
            wd.close()
        request.addfinalizer(finalizer)

    def test_input(self):
        wd.find_element_by_xpath(self.search_bar).send_keys("python"+Keys.ENTER)


