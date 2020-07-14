import unittest
import HtmlTestRunner
from settings import wd,url
testRunner = HtmlTestRunner.HTMLTestRunner(output=r'C:\Users\vidya gowda\PycharmProjects\Selenium1\Reports\htmlReports')

class LoginTest(unittest.TestCase):

    emailText = '//input[@id="username"]'
    pwdTxt = '//input[@name="pwd"]'
    loginBtn = "//div[text()='Login ']"

    def setUp(self):
        wd.get(url[2])
        wd.maximize_window()

    def tearDown(self):
        wd.close()

    def test_credentials(self):
        wd.implicitly_wait(30)
        wd.find_element_by_xpath(self.emailText).send_keys('admin')
        wd.find_element_by_xpath(self.pwdTxt).send_keys('manager')
        wd.find_element_by_xpath(self.loginBtn).click()

if __name__=="__main__":
    unittest.main(testRunner=testRunner,verbosity=2)
