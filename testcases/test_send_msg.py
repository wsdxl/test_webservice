"""
============================
Author  : XiaoLei.Du
Time    : 2019/12/19 21:26
E-mail  : 506615839@qq.com
File    : test_send_msg.py
============================
"""
import os
import random
import unittest
from library.ddt import ddt, data
from common.contans import DataDir
from common.read_excel import ReadExcel
from common.read_conf import conf
from common.my_logger import my_logger
from common.hande_db import HandDB
from common.hander_data import TestData, replace_data
from common.hander_webservice import HanderWebs

data_path = os.path.join(DataDir, 'cases.xlsx')


@ddt
class TestSendMsg(unittest.TestCase):
    excel = ReadExcel(data_path, 'send')
    datas = excel.read_excel()
    wb = HanderWebs()
    db = HandDB()

    @data(*datas)
    def test_sendmsg(self, case):
        pass
        url = conf.get('webservice', 'url') + case['url']
        mobile = self.rand_phone()
        ip = self.rand_ip()
        setattr(TestData, 'mobile', mobile)
        setattr(TestData, 'ip', ip)
        case['data'] = replace_data(case['data'])
        row = case['case_id'] + 1

        result = self.wb.send(url=url, interface=case['interface'], data=case['data'])

        try:
            self.assertEqual(case['expected'], str(result))
        except AssertionError as e:
            self.excel.write_excel(row=row, column=7, value='未通过')
            my_logger.info('用例-->{}:执行未通过'.format(case['title']))
            my_logger.error(e)
            raise e
        else:
            self.excel.write_excel(row=row, column=7, value='已通过')
            my_logger.info('用例-->{}:执行已通过'.format(case['title']))

    @classmethod
    def tearDownClass(cls):
        cls.db.close()

    def rand_phone(self):
        """随机生成手机号"""
        while True:
            item = ''
            for v in range(5):
                i = random.randint(0, 9)
                item += str(i)
            mobile = '136' + item + '150'
            # 查询数据库该号码是否存在
            count = self.db.get_count('SELECT * FROM sms_db_50.t_mvcode_info_1 WHERE Fmobile_no={};'.format(mobile))
            if count == 0:
                return mobile

    def rand_ip(self):
        ip = '{}.{}.{}.{}'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),
                                  random.randint(0, 255))
        return ip
