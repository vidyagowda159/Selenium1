from selenium import webdriver
wd = webdriver.Chrome(executable_path=r"C:\Users\vidya gowda\PycharmProjects\Selenium1\drivers\chromedriver.exe")

url=[r"https://www.google.com/",r"https://www.w3schools.com/python/",r"https://demo.actitime.com/login.do",r'https://www.makemytrip.com/']


option= webdriver.ChromeOptions()
option.headless=True