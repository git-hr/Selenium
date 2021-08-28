import sys
sys.path.append('D:\\workspace\\python')
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import time
import os
import HTMLTestRunner
class RegisterCase(unittest.TestCase):       
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.register = RegisterBusiness(self.driver)
    def tearDown(self):
        time.sleep(5)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                local_time = time.strftime('_%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
                file_path = os.path.join(os.getcwd(),'report',case_name + local_time + '.png')
                self.driver.save_screenshot(file_path)

        self.driver.close()
    # 注册成功
    def test_register_success(self):
        success = self.register.register_success('19198528521@163.com','19198528521','password','code1')
        self.assertFalse(success,'注册成功')
    # 邮箱输入错误
    def test_register_email_error(self):
        email_error = self.register.register_email_error('','name','password','code1')
        self.assertFalse(email_error,"注册成功，此条case失败")
    # 用户名输入错误
    def test_register_name_error(self):
        name_error = self.register.register_name_error('19198528521@163.com','','password','code1')
        self.assertFalse(name_error,"注册成功，此条case失败")
    # 密码输入错误
    def test_register_password_error(self):
        password_error = self.register.register_password_error('19198528521@163.com','name','','code1')
        self.assertFalse(password_error,"注册成功，此条case失败")
    # 验证码输入错误
    def test_register_code_error(self):
        code_error = self.register.register_code_error('19198528521@163.com','name','password','')
        self.assertFalse(code_error,"注册成功，此条case失败")


if __name__ == '__main__':
    report_dir = os.path.join(os.getcwd(),'report','report_01.html')
    f = open(report_dir,'wb')
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(RegisterCase('test_register_success'))
    runnner = HTMLTestRunner.HTMLTestRunner(stream=f,title="first report",description="321",verbosity=2)
    runnner.run(suite)