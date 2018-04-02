#!/usr/bin/env python
# coding=utf8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage


def sendtextmail(sender,pwd,receiver):
    # __init__(self, _text, _subtype='plain', _charset='us-ascii'):
    htmlmsg = """
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.baidu.com">百度一下</a></p>
    """
    msg = MIMEText(htmlmsg, 'html', 'utf-8')

    #msg = MIMEText('python test', 'plain', 'utf-8')
    msg['fRom'] = formataddr(["QQ邮箱", sender])  # 发件人邮箱昵称、发件人邮箱账号
    msg['to'] = receiver  # formataddr(["我", receiver])  # 收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = "python发送邮件测试"  # 标题
    print msg
    try:
        #smtpservice = smtplib.SMTP_SSL("smtp.qq.com",465)  #两种都可以实现  SMTP_SSL和SMTP的区别？？
        smtpservice = smtplib.SMTP("smtp.qq.com", 25)
        smtpservice.starttls()
        smtpservice.login(sender,pwd)
        #sendmail(self, from_addr, to_addrs, msg, mail_options=[],rcpt_options=[])
        smtpservice.sendmail(sender,receiver.split(','),msg.as_string())
        smtpservice.quit()
        print "邮件发送成功"
    except:
        print "邮件发送失败"
def sendextramail(sender,pwd,receiver):
    # 带附件的实例
    msg = MIMEMultipart()
    msg['From'] = formataddr(["QQ邮箱", sender])  # 发件人邮箱昵称、发件人邮箱账号
    msg['To'] = receiver  # formataddr(["我", receiver])  # 收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = "python发送邮件测试"  # 标题
    #邮件正文
    html_msg = """
    <p>python test</p>
    <p><a href ="http://www.baidu.com">百度一下</a></p>
    """
    # 邮件正文内容
    msg.attach(MIMEText(html_msg,'html','utf-8'))
    #添加第一个附件
    att1 = MIMEText(open('test.txt','rb').read(),'base64','utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment;filename = "test.txt"'
    msg.attach(att1)
    try:
        #smtpservice = smtplib.SMTP_SSL("smtp.qq.com",465)  #两种都可以实现  SMTP_SSL和SMTP的区别？？
        smtpservice = smtplib.SMTP("smtp.qq.com", 25)
        smtpservice.starttls()
        smtpservice.login(sender,pwd)
        #sendmail(self, from_addr, to_addrs, msg, mail_options=[],rcpt_options=[])
        smtpservice.sendmail(sender,receiver.split(','),msg.as_string())
        smtpservice.quit()
        print "邮件发送成功"
    except:
        print "邮件发送失败"
def sendpicturemail(sender,pwd,receiver):

    msg = MIMEMultipart()
    msg['From'] = formataddr(["QQ邮箱", sender])  # 发件人邮箱昵称、发件人邮箱账号
    msg['To'] = receiver#formataddr(["我", receiver])  # 收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = "python发送邮件测试"  # 标题
    #邮件正文
    html_msg = """
    <p>python test</p>
    <p><a href ="http://www.baidu.com">百度一下</a></p>
    <p><img src = "cid:image1"></p>
    """
    # 邮件正文是MIMEText:
    msg.attach(MIMEText(html_msg, 'html', 'utf-8'))

    fp = open('ver.png','rb')
    msgimage = MIMEImage(fp.read())
    fp.close()

    msgimage.add_header('Content-ID','<image1>')
    msg.attach(msgimage)
    # xlsx类型附件
    part = MIMEApplication(open(r'test.xlsx', 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="test.xlsx")
    msg.attach(part)

    # jpg类型附件
    part = MIMEApplication(open(r'test.png', 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename=('gbk', '', 'test.png'))
    msg.attach(part)

    # pdf类型附件
    part = MIMEApplication(open(r'test.pdf', 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="test.pdf")
    msg.attach(part)
    try:
        #smtpservice = smtplib.SMTP_SSL("smtp.qq.com",465)  #两种都可以实现  SMTP_SSL和SMTP的区别？？
        smtpservice = smtplib.SMTP("smtp.qq.com", 25)
        smtpservice.starttls()
        smtpservice.login(sender,pwd)
        #sendmail(self, from_addr, to_addrs, msg, mail_options=[],rcpt_options=[])
        smtpservice.sendmail(sender,receiver.split(','),msg.as_string())
        smtpservice.quit()
        print "邮件发送成功"
    except:
        print "邮件发送失败"
def test(flag):
    Form = "443245605@qq.com"
    Pwd = "zuovtsxbvrvgbhgc"
    To ='443245605@qq.com,17718412595@126.com'#"17718412595@126.com"#可发多个#"17718412595@126.com"
    if(flag == 1):
        sendtextmail(Form, Pwd, To)
    elif(flag == 2):
        sendextramail(Form, Pwd, To)
    elif(flag == 3):
        sendpicturemail(Form, Pwd, To)
if __name__ == '__main__':
    test(1)


