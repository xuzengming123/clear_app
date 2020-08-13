import logging
import time,os


class Logger(object):
    """封装日志模块"""
    def __init__(self):
        self.logger = logging.getLogger()

        # 设置输出的等级
        LEVELS = {'NOSET': logging.NOTSET,
                  'DEBUG': logging.DEBUG,
                  'INFO': logging.INFO,
                  'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR,
                  'CRITICAL': logging.CRITICAL}

        # log_path是存放日志的路径
        timestr = time.strftime('%Y_%m_%d', time.localtime(time.time()))
        log_dir = os.path.abspath('../Log')
        self.log_name = log_dir + r"\\" + timestr + '.log'

        #如果不存在就创建一个
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

        #日志文件地址
        logs_dir = r'E:\clear_test1\Log'
        self.logfilepath = os.path.join(logs_dir, self.log_name)



        #设置日志的输出等级
        self.logger.setLevel(logging.INFO)

        #日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

        ##日志输出到文件
        # 'a':追加
        # ’w‘:不追加
        fh = logging.FileHandler(self.logfilepath,mode='a',encoding='utf-8')
        fh.setLevel(logging.INFO)  #输出到file的log等级总开关
        #日志输出到控制台
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)#输出到控制台的log等级总开关

        #加载格式
        fh.setFormatter(self.formatter)
        console.setFormatter(self.formatter)

        #将logger添加到handler里面
        self.logger.addHandler(fh)
        self.logger.addHandler(console)

    def info(self,message):
        self.logger.info(message)

    def debug(self,message):
        self.logger.debug(message)

    def warning(self,message):
        self.logger.warning(message)

    def error(self,message):
        self.logger.error(message)



log = Logger()
if __name__ == '__main__':
    log.info('info')