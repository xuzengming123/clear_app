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
from Config.url_path import *
from Until.handle_log import log



class runmain(unittest.TestCase):
    def setUp(self):
        from Config.header import headers
        headers = headers

    def tearDown(self):
        pass

    def test_getAwardDesc(self):
        """获取中奖描述"""
        res = BaseRequest.run_main('get',getAwardDesc_url,header=headers)
        try:
            self.assertEqual(res['code'],'200',msg='接口返回失败')
            self.assertEqual(len(res['data']),10,msg='接口返回的中奖信息不是10条')
        except:
            log.info(res)

    def test_getRondaData(self):
        """获取当前时间的场次配置"""
        res = BaseRequest.run_main('get',getRondaData_url,header=headers)
        self.assertEqual(res['code'],'200',msg='%s'%res['msg'])

    def test_getAwardMsg(self):
        """今日客户获奖金币与刮奖次数"""
        res = BaseRequest.run_main('get',getAwardMsg_url,header=headers)
        self.assertEqual(res['code'],'200',msg='%s'%res['msg'])


    def test_areaOneOperation(self):
        """区域1刮奖专用"""
        res = BaseRequest.run_main('get',areaOneOperation_url,data={"id":8},header=headers)
        self.assertEqual(res['code'],'200',msg='%s'%res['msg'])

    def test_areaTwoOperation(self):
        """区域2刮奖专用"""
        res = BaseRequest.run_main('get',areaTwoOperation_url,data={"id":4,"gold":200},header=headers)
        self.assertEqual(res['code'],'200',msg='%s'%res['msg'])


#获取测试报告的输出路径
report_path = common.get_report_path()

if __name__ == '__main__':
    # unittest.main()
    run_main_tests = unittest.TestLoader().loadTestsFromTestCase(runmain)
    suite = unittest.TestSuite([run_main_tests])
    with open(report_path,'wb') as rp:
        runner = HTMLTestRunner(stream=rp,title='测试报告',description='执行情况',verbosity=2)
        runner.run(suite)
    # test_suite = unittest.defaultTestLoader.discover('E:\clear_test1\TestCase',pattern='*.py')
    # result = BeautifulReport(test_suite)
    # result.report(filename='测试报告',description='测试deafult',report_dir='E:\clear_test1\Report',theme='theme_deafult')

