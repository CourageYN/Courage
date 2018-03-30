#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib

def sendMail(body):
    smtp_server = 'smtp.163.com'
    from_mail = 'ynwangbiu@163.com'
    mail_pass = 'xxx'
    to_mail = ['876447556@qq.com']
    cc_mail = ['yaniray@yeah.com']
    from_name = 'monitor'
    subject = u'测试测试'.encode('gbk')   # 以gbk编码发送，一般邮件客户端都能识别



    mail = [
        "From: %s <%s>" % (from_name, from_mail),
        "To: %s" % ','.join(to_mail),   # 转成字符串，以逗号分隔元素
        "Subject: %s" % subject,
        "Cc: %s" % ','.join(cc_mail),
        "",
        body
        ]
    msg = '\n'.join(mail)  #
    try:
        s = smtplib.SMTP()
        s.connect(smtp_server, '25')
        s.login(from_mail, mail_pass)
        s.sendmail(from_mail, to_mail+cc_mail, msg)
        s.quit()
    except smtplib.SMTPException as e:
        print "Error: %s" %e
if __name__ == "__main__":
    sendMail("This is a test!")