# -*- coding:utf-8 -*-



import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "876447556@qq.com"  # 发件人用户名
mail_pass = "jejnzpmmtsjbbedb"  # 发件人口令,QQ邮箱是输入授权码,在qq邮箱设置里用验证过的手机发送短信获得,不含空格

sender = '876447556@qq.com'  # 与发件人用户名保持一致
receivers = "ynwangbiu@163.com"  # 收件人邮箱地址，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('内容', 'plain', 'utf-8')
message['From'] = Header("发件人", 'utf-8')
message['To'] = Header("you", 'utf-8')

subject = '标题'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print u"邮件发送成功"
except smtplib.SMTPException, e:
        print e

