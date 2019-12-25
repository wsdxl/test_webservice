"""
============================
Author  : XiaoLei.Du
Time    : 2019/12/19 19:33
E-mail  : 506615839@qq.com
File    : test.py
============================
"""
from suds.client import Client
import suds
#
# user_url = 'http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl'
#
# # 返回一个webservice对象
# web_s=Client(user_url)
# # print(web_s)
# # 准备测试用例数据
# data={"client_ip":"1.55.6.8","tmpl_id":"1","mobile":"13084187150"}
# # res=web_s.service.sendMCode(data)
# # print(dict(res))
# # 发送请求
# try:
#     res=web_s.service.sendMCode(data)
# except suds.WebFault as e:
#     print(dict(e.fault))
# else:
#     print(dict(res))

import random
from common.hande_db import HandDB
from common.hander_data import TestData,replace_data
from common.hander_webservice import HanderWebs
wb=HanderWebs()
db=HandDB()
url='http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl'
mobile="13679961150"
ip="183.255.24.191"
setattr(TestData,'mobile',mobile)
setattr(TestData,'ip',ip)
data='{"client_ip":"#ip#","tmpl_id":"1","mobile":"#mobile#"}'
data=replace_data(data)
# print(data)
interface="sendMCode"
result=wb.send(url,interface,data)
print(result)


