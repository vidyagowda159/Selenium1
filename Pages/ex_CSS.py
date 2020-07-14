from selenium.webdriver.common.by import By

from settings import url2,wd
import time
class CSS_selectors:

    def w3_CSS(self):
        wd.get(url2)
        wd.maximize_window()
        text_java=wd.find_element_by_css_selector('a[class="w3-bar-item w3-button"][title="JavaScript Tutorial"]').text
        wd.find_element_by_css_selector('a[class="w3-bar-item w3-button"][title="JavaScript Tutorial"]').click()
        print("text is : ",text_java)
        time.sleep(2)
        tagname=wd.find_element_by_class_name("w3-panel.w3-info.intro").tag_name
        print("tagname is : ",tagname)
        print(wd.find_element_by_id("belowtopnav").get_attribute("class"))
        #print(wd.find_element_by_css_selector('a[class="w3-bar-item w3-button"][title="JavaScript Tutorial"]').value_of_css_property("color"))
        #wd.find_element_by_css_selector("a#topnavbtn_tutorials").click()
        wd.find_element_by_css_selector("a.w3-bar-item.w3-button#topnavbtn_tutorials").click()
        time.sleep(2)
        text2 = wd.find_element_by_css_selector('div[class="w3-clear nextprev"]+div>a').text
        print(text2)
        wd.close()



obj=CSS_selectors()
obj.w3_CSS()