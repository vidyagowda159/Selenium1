from settings import wd,url
from selenium.webdriver.common.by import By

class locators:
    def basicLoc(self):
        wd.get(url)
        wd.maximize_window()
        data="python"
        wd.find_element(By.NAME,"q").send_keys(data)
        wd.find_element(By.NAME, "q").clear()
        print(wd.find_elements_by_class_name("Fx4vi"))

        #wd.find_element(By.ID,"gb_70").click()

        #wd.find_element_by_id("gb_70")
        #wd.find_element_by_class_name()


obj=locators()
obj.basicLoc()
