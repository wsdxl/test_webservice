"""
============================
Author  : XiaoLei.Du
Time    : 2019/12/19 20:44
E-mail  : 506615839@qq.com
File    : test1.py
============================
"""
from suds.client import Client
import suds

register_url = "http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
c = Client(register_url)
print(c)
data = {
    "verify_code": "557408",
    "user_id": "dxl20",
    "channel_id": 1,
    "pwd": "123456",
    "mobile": "13641878151",
    "ip": 1111
}
try:

    res = c.service.userRegister(data)
except suds.WebFault as e:
    print(dict(e.fault))
else:
    print(dict(res))


