import json
import pprint
import requests
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from Until.handle_excel import excel_data
from BeautifulReport.BeautifulReport import BeautifulReport
from Config.header import headers
from Until.handle_ini import handle_init
from Until.handle_common import common
from Until.handle_request import *
from Config.header import *
from Config.url_path import *
from Until.handle_log import log
from Until.handle_result import ExpectationResultMoed

class RunExcel(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_run_excel(self):
        #获取总行数
        rows = excel_data.get_rows()

        for i in range(rows-1):
            data = excel_data.get_rows_value(i+2)
            is_run = data[2]
            if is_run == 'yes':
                url = data[3]
                method = data[4]
                commom_header = data[5]
                result_method = data[9]
                ExpectationResult = data[10]
                if commom_header == 'yes':
                    commom_header = headers
                    res = BaseRequest.run_main(method,url,header=commom_header)
                    code_stutas = res['code']
                    message = res['message']
                    if result_method == 'mec':
                        excel_message = ExpectationResultMoed.get_excel_message(ExpectationResult,url,code_stutas)
                        if message == excel_message:
                            excel_data.excel_wirte_data(i+2,12,'测试通过')
                        else:
                            excel_data.excel_wirte_data(i+2,12, '测试失败')



if __name__ == '__main__':
    a = RunExcel()
    a.run()














