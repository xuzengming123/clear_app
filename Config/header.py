from Until.handle_common import common
import time

'''
公共参数
request-id	是	String	请求ID	全局唯一ID
request-agent	是	int	请求来源	1：android、2：iOS、3：PC、4：H5、5：wechat
device-id	是	String	设备ID	手机的硬件设备的唯一ID 即MEID
os-version	是	int	手机操作系统	0：android、1：iOS
sdk-version	是	String	SDK版本号	开发包具体的版本号
phone-model	是	String	手机型号	当前手机型号
market	是	String	应用渠道	应用下载渠道
app-version	是	String	app版本号	应用版本号，比如：1.0.0
app-name	是	string	APP名称	wz_clean 等等...
app-id	是	String	APP的唯一标识	由服务端提供
timestamp	是	long	请求时间戳	时间戳
sign	是	String	签名	具体算法见备注
customer-id	否	String	用户编号	登录后必传
access-token	否	String	访问令牌	登录后必传
sm-deviceid	否	String	数美指纹标识	数美指纹标识
gps-lng	否	String	经度	
gps-lat	否	String	纬度	
gt-id	否	String	个推id	
sdk-uid	否	String	大数据埋点用户标识	大数据埋点用户标识
'''

headers = {
"request-id":"71de5405-f6c5-4082-82a4-c5d6e9ce66a1",
"request-agent":"cn",
"device-id":"cb10cf945fe44801",
"os-version":"0",
"sdk-version":"26",
"phone-model":"MI 6",
"market":"gj_official",
"app-version":"3.0.2",
"app-name":"gj_clean",
"app-id":"wx646080363915ffe2",
"timestamp":str(round(time.time()*1000)),
"sign":str(common.get_sign()),
"customer-id":"no-login",
"Content-Type":"application/json; charset=utf-8",
"Referer":"http://wkkeeperh5.wukongclean.com/html/activitiesHtml/scratchCards/cardList.html?1596445",
"Origin":"http://wkkeeperh5.wukongclean.com"
}

if __name__ == '__main__':
    print(type(headers))
    print(headers)

