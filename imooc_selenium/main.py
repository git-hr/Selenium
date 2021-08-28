import sys
sys.path.append('D:/workspace/python')
from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('http://www.5itest.cn/register')

getcode = driver.find_element_by_id('getcode_num')
driver.save_screenshot('D:/imooc.png')
left = getcode.location['x']
top = getcode.location['y']

right = getcode.size['width'] + left
height = getcode.size['height'] + top
im = Image.open("D:/imooc.png")
img = im.crop((left,top,right,height))
img.save("D:/imooc1.png")

time.sleep(3)
driver.close()
# locator = (By.ID,"kw123")
# kw = driver.find_element_by_id('kw')

# send_kw = ''.join(random.sample('1234567890abcdefg',5)) + '@163.com'

# kw.send_keys(send_kw)
# value1 = kw.get_attribute('value')
# time.sleep(5)
# print(value1)
# driver.find_element_by_id('kw').send_keys('百度地图')
# driver.find_element_by_id('su').click()
# try :
#     WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))
#     print('Found')
#     driver.close()
# except:
#     print('NotFound')

