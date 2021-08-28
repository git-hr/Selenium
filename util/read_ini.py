import configparser

class ReadIni(object):
    def __init__(self,filename = None,node = None):
        if filename == None:
            filename = 'D:/workspace/python/config/LocalConfig.ini'
        if node == None:
            self.node = 'RegisterElements'
        self.cf = self.load_ini(filename)
    # 加载文件
    def load_ini(self,filename):
        cf = configparser.ConfigParser()
        cf.read(filename)
        return cf
    # 读取文件数据
    def get_value(self,key):
        cf_value = self.cf.get(self.node,key)
        return cf_value