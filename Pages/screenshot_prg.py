from selenium import webdriver
from settings import url
path=r'C:\Users\vidya gowda\PycharmProjects\Selenium1\drivers\chromedriver.exe'
class Headless_browser():
    def headless(self):
        driver=webdriver.Chrome(executable_path=path)
        driver.get(url[2])
        driver.save_screenshot(r'C:\Users\vidya gowda\PycharmProjects\Selenium1\screenshots\ss1.png')
        print(driver.title)
        print("launched successfully")
        driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys('admin')

        driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("manager")

        boolValue = driver.find_element_by_xpath('//input[@id="keepLoggedInCheckBox"]').is_selected()
        print("boolValue before is :", boolValue)
        driver.get_screenshot_as_file(r'C:\Users\vidya gowda\PycharmProjects\Selenium1\screenshots\\')

        if boolValue == False:
            driver.find_element_by_xpath('//input[@id="keepLoggedInCheckBox"]').click()
            boolValue = driver.find_element_by_xpath('//input[@id="keepLoggedInCheckBox"]').is_selected()
            print("boolValue after clicking is :", boolValue)
            driver.get_screenshot_as_file(r'C:\Users\vidya gowda\PycharmProjects\Selenium1\screenshots\ss3.png')
            print(driver.get_screenshot_as_png())

        else:
            print("it is selected")
        # //tagname[text()="value"]
        driver.find_element_by_xpath('//div[text()="Login "]').click()
        driver.get_screenshot_as_base64()
obj=Headless_browser()
obj.headless()
