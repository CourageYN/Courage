# -*- coding:utf-8 -*-



import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "876447556@qq.com"  # 发件人用户名
mail_pass = "jejnzpmmtsjbbedb"  # 发件人口令

sender = '876447556@qq.com'
receivers = "ynwangbiu@163.com"

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

