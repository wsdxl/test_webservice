"""
============================
Author  : XiaoLei.Du
Time    : 2019/12/19 22:32
E-mail  : 506615839@qq.com
File    : test_register.py
============================
"""
import os
import random
import unittest
from library.ddt import ddt, data
from common.contans import DataDir
from common.read_excel import ReadExcel
from common.read_conf import conf
from common.hander_data import TestData, replace_data
from common.hander_webservice import HanderWebs
from common.my_logger import my_logger
from common.hande_db import HandDB

data_path = os.path.join(DataDir, 'cases.xlsx')


@ddt
class TestRegister(unittest.TestCase):
    excel = ReadExcel(data_path, 'register')
    datas = excel.read_excel()
    wb=HanderWebs()
    db = HandDB()

    @data(*datas)
    def test_register(self, case):
        url = conf.get('webservice', 'url') + case['url']
        mobile=self.ram_phone()
        ip=self.ram_ip()
        code = self.get_code(mobile, ip)
        # 获取用户名
        user_num = conf.getint('test_data', 'user_num') + 1
        conf.writeconf('test_data', 'user_num', str(user_num))
        user_id = 'dxl20' + str(user_num)

        setattr(TestData,'code',code)
        setattr(TestData,'user_id',user_id)
        setattr(TestData,'mobile',mobile)
        setattr(TestData,'ip',ip)

        case['data'] = replace_data(case['data'])
        row = case['case_id'] + 1

        result =self.wb.send(url=url,interface=case['interface'],data=case['data'])

        try:
            self.assertEqual(case['expected'],str(result))
        except AssertionError as e:
            self.excel.write_excel(row=row, column=7, value='未通过')
            my_logger.info('用例-->{}:执行未通过'.format(case['title']))
            my_logger.error(e)
            raise e
        else:
            self.excel.write_excel(row=row, column=7, value='已通过')
            my_logger.info('用例-->{}:执行未通过'.format(case['title']))

    def ram_phone(self):
        '''随机生成手机号码'''
        while True:
            item = ''
            for i in range(5):
                p = random.randint(0, 9)
                item += str(p)
            mobile = '136' + item + '150'
            # 查询数据库中号码是否存在
            count = self.db.get_count('select * from sms_db_50.t_mvcode_info_1 where Fmobile_no={}'.format(mobile))
            if count == 0:
                return mobile

    def ram_ip(self):
        ip="{}.{}.{}.{}".format(random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))
        return ip

    def get_code(self, phone, ip):
        """·
        获取验证码
        :param phone: 手机号码
        :return: 该手机号生成的验证码
        """
        # 生成验证码的方法
        url = "http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
        # 发请求生成验证码
        response = self.wb.send(url=url, interface='sendMCode',
                                    data={"client_ip": ip, "tmpl_id": '1', "mobile": phone})
        # 获取数据库中的验证码
        sql = "select Fverify_code from sms_db_50.t_mvcode_info_1 where Fmobile_no = {} order by Fsend_time desc limit 1".format(
            phone)
        code = self.db.get_one(sql)[0]
        return code

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

