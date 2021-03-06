from util.read_ini import ReadIni
from selenium import webdriver

class FindElement(object):
    def __init__(self,driver):
        self.driver = driver
        
    # 查找元素
    def get_element(self,key):
        self.read_ini = ReadIni()
        data = self.read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'classname':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None
