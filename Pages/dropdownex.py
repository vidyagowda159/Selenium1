from selenium.webdriver.support.select import Select
from settings import wd

path=r'C:\Users\vidya gowda\PycharmProjects\Selenium1\htmlFiles\Select_dropdown.html'
import time

class dd:

    def ex1(self):
        wd.get(path)
        element=wd.find_element_by_id("cars")
        time.sleep(2)
        s_obj=Select(element)
        s_obj.select_by_value("sub1")
        time.sleep(2)
        s_obj.select_by_index(3)
        time.sleep(2)
        s_obj.select_by_visible_text("Mysore")
        time.sleep(2)
        value1=s_obj.first_selected_option
        print("first option",value1.text)
        print("Options before deselecting")
        options=s_obj.all_selected_options
        for i in options:
            print(i.text)

        print(s_obj.is_multiple)
        print("Options after deselecting")

        '''
        s_obj.deselect_by_index(2)
        time.sleep(2)
        s_obj.deselect_by_value("sub1")
        time.sleep(2)
        s_obj.deselect_by_visible_text("Mysore")
        time.sleep(2)
        '''
        s_obj.deselect_all()
        options = s_obj.all_selected_options
        for i in options:
            print(i.text)
        opt=s_obj.options
        for i in opt:
            print(i.text)


obj=dd()
obj.ex1()