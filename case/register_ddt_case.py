import sys
sys.path.append('D:\\workspace\\python')
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import time
import os
import HTMLTestRunner
import ddt
from util.excel_util import ExcelUtil
from log.user_log import Userlog
ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
class RegisterDdtCase(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.register = RegisterBusiness(self.driver)
        self.logger.debug(self._testMethodName)
    def tearDown(self):
        time.sleep(5)
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                local_time = time.strftime('_%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
                file_path = os.path.join(os.getcwd(),'report',case_name + local_time + '.png')
                self.driver.save_screenshot(file_path)

        self.driver.close()
    @classmethod
    def setUpClass(cls):
        cls.log = Userlog()
        cls.logger = cls.log.get_log()
    @classmethod
    def tearDownClass(cls):
        cls.log.log_close()
    # @ddt.data(
    #     ['19198528521@163.com','19198528521','password','code1','code_text_error'],
    #     ['@163.com','19198528521','password','code1','user_email_error'],
    #     ['19198528521@163.com','19198528521','password','code1','user_email_error']
    # )
    # @ddt.unpack
    @ddt.data(*data)
    def test_register(self,data):
        email,name,password,code,assertCode = data
        success = self.register.register_function(email,name,password,code,assertCode)
        self.assertFalse(success,'注册结束')


if __name__ == '__main__': 
    report_dir = os.path.join(os.getcwd(),'report','report_01.html')
    f = open(report_dir,'wb')
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(RegisterDdtCase)
    # suite.addTest(RegisterDdtCase('test_register'))
    runnner = HTMLTestRunner.HTMLTestRunner(stream=f,title="first report",description="321",verbosity=2)
    runnner.run(suite)