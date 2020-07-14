from settings import wd,url
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class AC:

    actions=ActionChains(wd)
    def Se
    def login(self):
        wd.get(url[2])
        wd.maximize_window()
        print("in login")
        wd.find_element_by_xpath('//input[@placeholder="Username"]').send_keys('admin')
        wd.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("manager")
        wd.find_element_by_xpath('//div[text()="Login "]').click()

    def homePage(self):
        wd.implicitly_wait(10)
        print("in homepage")
        element = wd.find_element_by_xpath('//a[contains(text(),"Lock Time-Track")]')
        self.actions.move_to_element(element).perform()
        self.actions.context_click(element).perform()
        loc= wd.find_element_by_xpath('//td[text()="Enter Time-Track"]').location
        x=loc['x']
        y=loc['y']
        self.actions.move_by_offset(x,y).perform()
        self.actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()


    def actiTime_actions(self):
        print("in actitime actions")
        self.login()
        print("done with logging in")
        self.homePage()
        print("done with moving the cursor")


obj=AC()
obj.actiTime_actions()