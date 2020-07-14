from settings import wd,url
wd.get(url[2])
wd.maximize_window()
wd.find_element_by_id("username").send_keys("admin")
wd.find_element_by_name("pwd").send_keys("manager")
wd.find_element_by_xpath('//div[text()="Login "]').click()
wd.add_cookie({"name":"admin","value":"python"})
cookie_value=wd.get_cookies()
for i in cookie_value:
    print(i)
wd.delete_cookie("admin")
print(wd.get_cookies())
