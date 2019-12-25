"""
============================
Author  : XiaoLei.Du
Time    : 2019/11/23 17:22
E-mail  : 506615839@qq.com
File    : run_suite.py
============================
"""
import os
import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner
from common.contans import CaseDir,ReportDir
from testcases import test_send_msg,test_register
from common.read_conf import conf
from common.send_email import senf_email
title=conf.get('report','title')
description=conf.get('report','description')
tester=conf.get('report','tester')

# 第一步：新建测试套件
suite=unittest.TestSuite()
# 第二步：加载测试用例到测试套件
loader=unittest.TestLoader()
case_path=os.path.join(CaseDir)
suite.addTest(loader.discover(case_path))
# suite.addTest(loader.loadTestsFromModule(test_register))
# 第三步：新建测试用例启动器
report_path=os.path.join(ReportDir,'report.html')
with open(report_path,'wb') as f:
    runner=HTMLTestRunner(
        stream=f,
        title=title,
        description=description,
        tester=tester
        )
    # 第四步：运行用例启动器
    runner.run(suite)
# email=senf_email(report_path)