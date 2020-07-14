from settings import wd
import time
class alert:
    path = r'C:\Users\vidya gowda\PycharmProjects\Selenium1\htmlFiles\alert and pop up handling\simple_alert.html'
    path_con=r'C:\Users\vidya gowda\PycharmProjects\Selenium1\htmlFiles\alert and pop up handling\confirmation_alert.html'
    path_prompt=r'C:\Users\vidya gowda\PycharmProjects\Selenium1\htmlFiles\alert and pop up handling\Prompt_alert.html'

    def simple_alert(self):
        wd.get(self.path)
        wd.find_element_by_name("alert").click()
        time.sleep(2)
        alert_obj=wd.switch_to.alert
        alert_obj.accept()
        time.sleep(2)
        wd.close()

    def confirmation_alert(self):
        wd.get(self.path_con)
        wd.find_element_by_name("alert").click()
        alert_obj=wd.switch_to.alert
        alert_obj.dismiss()
        time.sleep(2)
        wd.close()

    def prompt_alert(self):
        wd.get(self.path_prompt)
        wd.find_element_by_name("employeeLogin").click()
        alert_obj=wd.switch_to.alert
        time.sleep(2)
        print(alert_obj.text)
        alert_obj.send_keys("vidya")
        time.sleep(2)
        alert_obj.accept()
        print(alert_obj.text)
        alert_obj.accept()



obj=alert()
obj.prompt_alert()