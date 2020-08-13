import os
import time
from hashlib import sha256
import base64
import hmac

class Common:
    def get_timestamp(self):
        '''
        获取13位时间戳
        :return:
        '''
        timestamp = str(round(time.time()*1000))
        return timestamp

    def get_sign(self):
        '''
        签名
        :return: 签名（字符串）
        '''
        timestamp = str(round(time.time() * 1000))
        appId = '48410f57d9eb4cd983a535227bd5c722'
        data = appId + timestamp
        key = '69c309a1039f4a708c211153733cfh22'
        secrets = key.encode('utf-8')
        message = data.encode('utf-8')
        sign = base64.b64encode(hmac.new(secrets,message,digestmod=sha256).digest())
        sign = str(sign,'utf-8')
        return sign

    def get_report_path(self):
        '''
        获取报告输出路径
        :return:
        '''
        dirss = os.path.abspath('../Report/')
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        HtmlFile = os.path.join(dirss, 'Testreport' + now + '.html')
        return HtmlFile




common = Common()
if __name__ == '__main__':
    print(common.get_timestamp())
    print(common.get_sign())