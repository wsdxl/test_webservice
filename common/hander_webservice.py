"""
============================
Author  : XiaoLei.Du
Time    : 2019/12/21 15:54
E-mail  : 506615839@qq.com
File    : hander_webservice.py
============================
"""
import suds
from suds.client import Client


class HanderWebs(object):
    """发送webservice请求"""

    def send(self,url,interface,data,):
        web_s=Client(url)
        try:
            res = eval("web_s.service.{}({})".format(interface, data))
        except suds.WebFault as e:
             return (dict(e.fault))
        else:
            return (dict(res))

    # def send(self, url, interface, data):
    #     # 发送请求获取地址接口
    #     wb = Client(url=url)
    #     method = getattr(wb.service, interface)
    #     try:
    #         respone = method(data)
    #     except suds.WebFault as e:
    #         return dict(e.fault)
    #     else:
    #         return dict(respone)


if __name__ == "__main__":
    wb = HanderWebs()
    url = 'http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl'
    data = {"client_ip": "1.2.6.8", "tmpl_id": "1", "mobile": "13055387150"}
    interface = "sendMCode"
    res=wb.send(url,interface,data)
    print(res,type(res))
