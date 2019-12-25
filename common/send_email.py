"""
============================
Author  : XiaoLei.Du
Time    : 2019/12/17 21:43
E-mail  : 506615839@qq.com
File    : send_email.py
============================
"""
import os
from common.contans import ReportDir
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
'''
通过邮件发送测试报告
报告做为邮件附件的方式进行发送
'''
def senf_email(file_path):
    # 第一步：连接到smtp服务器
    smtp = smtplib.SMTP_SSL(host='smtp.qq.com', port=465)

    # 第二步：登录服务器
    smtp.login('506615839@qq.com', 'hbngnzxicsmebjgh')

    # 第三步：准备邮件
    # 第1步：准备内容
    from_user = '506615839@qq.com'
    to_user = '530768572@qq.com'
    subject = '发送测试报告'
    content = 'python期api测试报告'
    # 读取报告文件内容
    file_content = open(file_path, 'rb').read()

    # 第2步：构造邮件
    # (1)、构造一封多组件邮件
    msg = MIMEMultipart()
    # （2）、往多组件邮件中加入文本内容
    text_msg = MIMEText(content, _subtype='plain', _charset='utf8')
    msg.attach(text_msg)
    # （3）、往多组件邮件中加入附件文件
    file_msg = MIMEApplication(file_content)
    file_msg.add_header('content-disposition', 'attachment', filename='api_report.html')
    msg.attach(file_msg)
    # （4）、添加发件人、收件人和邮件主题
    msg['FROM'] = from_user
    msg['TO'] = to_user
    msg['SUBJECT'] = subject
    # 第四步：发送邮件
    # print(msg)
    smtp.send_message(msg, from_addr='506615839@qq.com', to_addrs='530768572@qq.com')



