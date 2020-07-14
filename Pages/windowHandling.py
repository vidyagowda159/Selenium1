from selenium.common.exceptions import StaleElementReferenceException

from settings import wd,url

class handling:

    def win_handling(self,pageTitle):
        handles = wd.window_handles
        for i in handles:
            wd.switch_to.window(i)
            title_handle = wd.title
            if title_handle != pageTitle:
                wd.switch_to.window(i)
                break

    def fk_login(self):
        wd.get(url[3])
        wd.maximize_window()

        wd.implicitly_wait(30)
        #wd.find_element_by_xpath('//span[text()="Hotels"]').click()
        bool_value=wd.find_element_by_xpath('//p[text()="Login/Signup to earn ₹555 instantly"]').is_displayed()

        if bool_value==True:
            wd.find_element_by_xpath('//div[@data-cy="googleLogin"]').click()
        else:
            wd.find_element_by_xpath('//p[contains(text(),"Login or Create Account")]').click()
            wd.find_element_by_xpath('//div[@data-cy="googleLogin"]').click()

        pageTitle=wd.title
        print(pageTitle)
        self.win_handling(pageTitle)
        pageTitle = wd.title
        print(pageTitle)
        pageTitle1=wd.title
        print(pageTitle1)
        wd.find_element_by_id("identifierId").send_keys('vidyashree.temp15@gmail.com')
        wd.find_element_by_xpath('//span[text()="Next"]').click()
        wd.find_element_by_xpath('//input[@name="password"]').send_keys('7349614959')
        nextElement=wd.find_element_by_xpath('//span[text()="Next"]')
        
        try:
            nextElement.click()
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying to type password, trying to find element again')
            nextElement = wd.find_element_by_xpath('//span[text()="Next"]')
            nextElement.click()

        self.win_handling(pageTitle1)
        pageTitle1 = wd.title
        print(pageTitle1)
        print("after switching back")
        wd.find_element_by_xpath('//li[@class="   menu_Hotels "]').click()



obj=handling()
obj.fk_login()