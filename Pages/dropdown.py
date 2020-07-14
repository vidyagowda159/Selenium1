from selenium.webdriver.support.select import Select
from settings import wd
class dd:
    def drop(self):
        path=r'C:\Users\vidya gowda\PycharmProjects\Selenium1\htmlFiles\Select_dropdown.html'
        wd.get(path)
        wd.maximize_window()
        object=wd.find_element_by_xpath('//select[@name="cars"]')
        s=Select(object)
        print(s.is_multiple)
        r1=s.options
        for i in r1:
            print(i.text)

        print(s.first_selected_option)
        print(s.select_by_value("sub2"))
obj=dd()
obj.drop()
