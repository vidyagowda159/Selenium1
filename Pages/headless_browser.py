from selenium import webdriver
from settings import url
path=r'C:\Users\vidya gowda\PycharmProjects\Selenium1\drivers\chromedriver.exe'
class Headless_browser():
    def headless(self):
        option=webdriver.ChromeOptions()
        option.headless=True
        driver=webdriver.Chrome(executable_path=path,options=option)
        driver.get(url[2])
        print(driver.title)
        print("launched successfully")
obj=Headless_browser()
obj.headless()



