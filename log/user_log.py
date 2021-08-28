import logging
import os.path
import time

class Userlog():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 控制台输出日志
        # consle = logging.StreamHandler()
        # logger.addHandler(consle)
        # 文件输出日志
        rq = time.strftime('%Y%m%d%H', time.localtime(time.time()))
        # log_path = os.path.dirname(__file__) + '/logs/'
        log_path = os.path.dirname(__file__) + '/logs/'
        log_name = log_path + rq + '.log'
        logfile = log_name
        self.file_handle = logging.FileHandler(logfile)
        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)
        # self.logger.debug("this is a debug message")
    def get_log(self):
        return self.logger
    def log_close(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()