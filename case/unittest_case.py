import unittest
class UnittestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('case start')

    @classmethod
    def tearDownClass(cls):
        print('case down')
        
    def setUp(self):
        print('set up')
    def tearDown(self):
        print('tear down')
    def testcase01(self):
        print("case--------01")
    @unittest.skip('不执行代码示例')
    def testcase02(self):
        print("case--------02") 
    def testcase03(self):
        print("case--------03")

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(UnittestCase('testcase03'))
    suite.addTest(UnittestCase('testcase01'))
    suite.addTest(UnittestCase('testcase02'))
    unittest.TextTestRunner().run(suite)