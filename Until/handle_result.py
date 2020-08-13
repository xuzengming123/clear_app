import os,sys,json

class ExpectationResultMoed:
    @classmethod
    def get_excel_message(cls,message_data,url,code):
        '''
        从Excel文件中获取code对应的message信息
        :param message_data:
        :param key:
        :param code:
        :return:
        '''
        message_data = json.loads(message_data)
        message_list = message_data.get(url)
        if message_list != None:
            for i in message_list:
                mes = i.get(str(code))
                if mes:
                    return mes
        return None

    def get_result_from_excel(cls,messageData,url,status):
        '''
        从excel中获取预期结果。
        :param messageData: 接口数据
        :param url: 接口名
        :param status: 返回的状态
        :return:
        '''
        message_data = json.loads(messageData)
        if messageData:
            message_list = message_data.get(url)
            if message_list != None:
                for i in message_list:
                    mes = i.get(status)
                    if mes:
                        return mes
            return None
        return '该单元格没有数据'
er = ExpectationResultMoed()

if __name__ == '__main__':
    md = {"guaGuaActivity/getAwardDesc":[
{"200": "请求成功"},
{"1001": "网络异常，请稍后重试"},
{"3103": "账户不存在"},
{"200": "请求成功"}
]
}
    url = 'guaGuaActivity/getAwardDesc'
    code = '200'
    print(er.get_excel_message(md,url,code))

    re_md = {
    "requestId": 'null',
    "timestamp": 1597285604678,
    "code": "200",
    "message": "请求成功",
    "data": [
        "恭喜那些花儿获得大奖，提现4元现金",
        "恭喜星星获得大奖，提现4元现金",
        "恭喜杰伦粉获得大奖，提现2元现金",
        "恭喜糖宝获得大奖，提现2元现金",
        "恭喜相爱一生获得大奖，提现20元现金",
        "恭喜诺诺获得大奖，提现88元现金",
        "恭喜丫头获得大奖，提现2元现金",
        "恭喜大熊获得大奖，提现10元现金",
        "恭喜白百合获得大奖，提现8元现金",
        "恭喜笑笑获得大奖，提现8元现金"
    ]
}



