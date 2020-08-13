import requests
import os,json
import urllib3
from Until.handle_ini import handle_init
from Config.header import headers
from Until.handle_header import ahv

class BaseRequest:
    @classmethod
    def send_get(cls,url,data=None,cookies=None,get_cookie=None,header=None):
        urllib3.disable_warnings()
        response = requests.get(url=url,params=data,cookies=cookies,headers=header,verify=False)
        # if get_cookie != None:
        #     cookie_value_jar = response.cookies
        #     cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
        #     write_cookie(cookie_value,get_cookie['is_cookie'])
        res = response.text
        return res
    @classmethod
    def send_post(cls,url,data=None,cookies=None,get_cookie=None,header=None):
        urllib3.disable_warnings()
        response = requests.post(url=url,data=data,cookies=cookies,headers=header,verify=False)
        # if get_cookie != None:
        #     cookie_value_jar = response.cookies
        #     cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
        #     write_cookie(cookie_value,get_cookie['is_cookie'])
        res = response.text
        return res
    @classmethod
    def run_main(cls,method,url,data=None,cookies=None,get_cookie=None,header=None):
        base_url = handle_init.get_inivalue('online_host','server')
        if 'https' not in url:
            url = base_url + url
        if method == 'get':
            res = cls.send_get(url,data,cookies,get_cookie,header)
        else:
            res = cls.send_post(url,data,cookies,get_cookie,header)
        try:
            res = json.loads(res)
        except:
            return res
        return res

if __name__ == '__main__':

    header = headers
    header1 = ahv.add_to_header('xzm','asd')
    res = BaseRequest.run_main('post','/guaGuaActivity/getAwardDesc',header=header1)
    print(res)
