import ddt
import unittest
@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @ddt.data(
        ['1','2'],
        ['3','4'],
        ['5','6']
    )
    @ddt.unpack
    def test_add(self,a,b):
        print(int(a)+int(b))

if __name__ == '__main__':
    unittest.main()