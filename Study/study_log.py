import logging
import time
#1\日志级别
# 默认日志级别：warning，低于这个级别，就不会显示出来
'''
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
'''

# 设置日志级别
'''
logging.basicConfig(level=logging.INFO)
logging.debug('debug')
logging.info('info')
'''

#2\名词解释
'''
logging.Formatter:日志输出格式
logging.Logger:Logger模块的主体，主要进行以下工作：
1、为程序提供记录日志的接口
2、判断日志所处的级别，并判断是否要过滤
3、根据其日志级别，并将该条日志分发给不同的handle
常用函数有：
Logging.setLevel()设置日志级别
logging.addHandle()和logging.removeHandle()添加和删除一个Handle
Logging.addFilter()添加一个Filter，过滤作用
Logging.Handle:Handle基于日志级别对日志进行分发，如设置为WARNING级别的Handle只会处理WARNING以上级别的日志
setLevel()设置级别
setFormatter():设置Formatter
'''

#3\日志输出-控制台
'''
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')# logging.basicConfig函数对日志的输出格式及方式做相关配置
# 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
logging.info('info')                #2020-08-07 15:40:22,594 - handle_log.py[line:40] - INFO: info
logging.debug('debug')              #2020-08-07 15:40:22,594 - handle_log.py[line:41] - DEBUG: debug
logging.warning('warning')          #2020-08-07 15:40:22,594 - handle_log.py[line:42] - WARNING: warning
logging.error('error')              #2020-08-07 15:40:22,595 - handle_log.py[line:43] - ERROR: error
logging.critical('critical')        #2020-08-07 15:40:22,595 - handle_log.py[line:44] - CRITICAL: critical
'''


'''
#4\日志输出-文件
import logging
import os.path
import time
logger = logging.getLogger()
logger.setLevel(logging.INFO)   #Log等级总开关
第二步，创建一个handler，用于写入日志文件
rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
log_path = os.path.dirname(os.getcwd() + '/Study/')
log_name = log_path + rq + '.log'
logfile = log_name
fh = logging.FileHandler(logfile,mode='w')
fh.setLevel(logging.DEBUG)  #输出到file的log等级总开关
第三步，定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
fh.setFormatter(formatter)
第四步，将logger添加到handler里面
logger.addHandler(fh)
日志
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

'''


# 5\日志输出-控制台和文件
import logging
import os.path
import time
logger = logging.getLogger()
logger.setLevel(logging.INFO)   #Log等级总开关
'''第二步，创建一个handler，用于写入日志文件'''
rq = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
log_path = os.path.dirname(os.getcwd() + '/Study/')
log_name = log_path + rq + '.log'
logfile = log_name
#日志输出到文件
fh = logging.FileHandler(logfile,mode='w')
fh.setLevel(logging.DEBUG)  #输出到file的log等级总开关
#日志输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)#输出到控制台的log等级总开关
'''第三步，定义handler的输出格式'''
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
fh.setFormatter(formatter)
'''第四步，将logger添加到handler里面'''
logger.addHandler(fh)
'''日志'''
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')