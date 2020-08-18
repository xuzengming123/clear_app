import json
import pprint
import requests
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from Until.handle_excel import excel_data
from Config.header import headers
from Until.handle_ini import handle_init
from Until.handle_common import common
from Until.handle_request import *
from Config.header import *
from Until.handle_header import ath
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
                commom_header = data[5]   #公共header
                add_header_value = data[6]  #接口独有header字段
                body1 = data[7]       #data
                body1_is_must = data[8]    #data是否必传
                result_method = data[9]     #预期结果方式
                ExpectationResult = data[10]   #预期结果
                #公共header是否追加或者不追加
                if commom_header == 'yes':
                    commom_header = headers
                    if body1 == 'no':
                        data = None
                    else:
                        data = json.loads(body1)
                    res = BaseRequest.run_main(method,url,data=data,header=commom_header)
                    code_stutas = res['code']
                    message = res['message']
                    #预期结果方式
                    if result_method == 'mec':
                        excel_message = ExpectationResultMoed.get_excel_message(ExpectationResult,url,code_stutas)
                        if message == excel_message:
                            excel_data.excel_wirte_data(i+2,12,str(res))
                            excel_data.excel_wirte_data(i + 2, 13, 'pass')
                        else:
                            excel_data.excel_wirte_data(i+2,12,str(res))
                            excel_data.excel_wirte_data(i + 2, 12, 'fail')
                    if result_method == 'json':
                        if code_stutas == '200':
                            status_str = 'sucess'
                        else:
                            status_str = 'error'
                        # 通过excel文件获取预期结果
                        excel_result = ExpectationResultMoed.get_excel_message(ExpectationResult, url, status_str)
                        # 开始校验结果
                        result = ExpectationResultMoed.handle_result_json(excel_result,res)
                        if result:
                            excel_data.excel_wirte_data(i + 2, 12, str(res))
                            excel_data.excel_wirte_data(i + 2, 13, 'pass')
                        else:
                            excel_data.excel_wirte_data(i + 2, 12, str(res))
                            excel_data.excel_wirte_data(i + 2, 13, 'fail')

                if commom_header == 'add_to':
                    commom_header = ath.add_to_header(json.loads(add_header_value))
                    if body1 == 'no':
                        data = None
                    else:
                        data = json.loads(body1)
                    res = BaseRequest.run_main(method,url,data=data,header=commom_header)
                    code_stutas = res['code']
                    if 'msg' in res:
                        msg = res['msg']
                        if result_method == 'mec':
                            excel_message = ExpectationResultMoed.get_excel_message(ExpectationResult,url,code_stutas)
                            if msg == excel_message:
                                excel_data.excel_wirte_data(i+2,12,str(res))
                                excel_data.excel_wirte_data(i + 2, 13, 'pass')
                            else:
                                excel_data.excel_wirte_data(i+2,12,str(res))
                                excel_data.excel_wirte_data(i + 2, 13, 'fail')
                        if result_method == 'json':
                            if code_stutas == '200':
                                status_str = 'sucess'
                            else:
                                status_str = 'error'
                            # 通过excel文件获取预期结果
                            excel_result = ExpectationResultMoed.get_excel_message(ExpectationResult, url, status_str)
                            # 开始校验结果
                            result = ExpectationResultMoed.handle_result_json(excel_result, res)
                            if result:
                                excel_data.excel_wirte_data(i + 2, 12, str(res))
                                excel_data.excel_wirte_data(i + 2, 13, 'pass')
                            else:
                                excel_data.excel_wirte_data(i + 2, 12, str(res))
                                excel_data.excel_wirte_data(i + 2, 13, 'fail')
                    else:
                        message = res['message']
                        if result_method == 'mec':
                            excel_message = ExpectationResultMoed.get_excel_message(ExpectationResult,url,code_stutas)
                            if message == excel_message:
                                excel_data.excel_wirte_data(i+2,12,str(res))
                                excel_data.excel_wirte_data(i + 2, 13, 'pass')
                            else:
                                excel_data.excel_wirte_data(i+2,12,str(res))
                                excel_data.excel_wirte_data(i + 2, 13, 'fail')
                        if result_method == 'json':
                            if code_stutas == '200':
                                status_str = 'sucess'
                            else:
                                status_str = 'error'
                            # 通过excel文件获取预期结果
                            excel_result = ExpectationResultMoed.get_excel_message(ExpectationResult,url,status_str)
                            # 开始校验结果
                            result = ExpectationResultMoed.handle_result_json(excel_result, res)
                            if result:
                                excel_data.excel_wirte_data(i + 2, 12, str(res))
                                excel_data.excel_wirte_data(i + 2, 13, 'pass')
                            else:
                                excel_data.excel_wirte_data(i + 2, 12, str(res))
                                excel_data.excel_wirte_data(i + 2, 13, 'fail')




if __name__ == '__main__':
    a = RunExcel()
    a.run()














