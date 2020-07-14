from PIL import Image
from settings import wd,url

wd.get(url[0])
wd.maximize_window()
element=wd.find_element_by_xpath('//img[@id="hplogo"]')
loc=element.location
print(loc)
siz=element.size
print(siz)
wd.save_screenshot(r'C:\Users\vidya gowda\PycharmProjects\Selenium1\screenshots\googlePage.png')
orignal_pic=Image.open(r'C:\Users\vidya gowda\PycharmProjects\Selenium1\screenshots\googlePage.png')
x=loc["x"]
y=loc["y"]
w=x+siz["width"]
h=y+siz["height"]
crop_attr=(x,y,w,h)

crop_img=orignal_pic.crop(crop_attr)
crop_img.save(r'C:\Users\vidya gowda\PycharmProjects\Selenium1\screenshots\crop.png')

wd.close()



