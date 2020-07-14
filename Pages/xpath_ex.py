from settings import wd,url
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class ex_xpath:

    def actiLogin(self):
        options=webdriver.ChromeOptions()
        options.headless=True
        options.add_argument("headless")

        wd.implicitly_wait(10)
        wd.get(url[2])
        wd.maximize_window()

        wd.find_element_by_xpath('//input[@placeholder="Username"]').send_keys('admin')

        wd.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("manager")

        boolValue=wd.find_element_by_xpath('//input[@id="keepLoggedInCheckBox"]').is_selected()
        print("boolValue before is :" ,boolValue)

        if boolValue==False:
            wd.find_element_by_xpath('//input[@id="keepLoggedInCheckBox"]').click()
            boolValue = wd.find_element_by_xpath('//input[@id="keepLoggedInCheckBox"]').is_selected()
            print("boolValue after clicking is :", boolValue)

        else:
            print("it is selected")
        #//tagname[text()="value"]
        wd.find_element_by_xpath('//div[text()="Login "]').click()
        #//tagname[normalize-space(source)="value"] ; source --> text() or attribute
        #//tagname[contains(source,"value")] ; source --> text() or attribute
        #//tagname[starts-with(source,"value")] : source --> text() or attribute
        #(//xpath)[n] : n>0

obj = ex_xpath()
obj.actiLogin()



