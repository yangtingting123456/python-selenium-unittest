# import smtplib
# import email.mime.multipart
# import email.mime.text
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
#
# def send_email(smtpHost,port, sendAddr, password, recipientAddrs, subject='', content=''):
#     msg = email.mime.multipart.MIMEMultipart()
#     msg['from'] = sendAddr
#     msg['to'] = recipientAddrs#多个收件人的邮箱应该放在字符串中,用字符分隔, 然后用split()分开,不能放在列表中, 因为要使用encode属性
#     msg['subject'] = subject
#     content = content
#     txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
#     msg.attach(txt)
#     print("准备添加附件...")
#     # 添加附件，从本地路径读取。如果添加多个附件，可以定义part_2,part_3等，然后使用part_2.add_header()和msg.attach(part_2)即可。
#     part = MIMEApplication(open('‪D:\\result\\result.html','rb').read())
#     part.add_header('Content-Disposition', 'attachment', filename="result.html")#给附件重命名,一般和原文件名一样,改错了可能无法打开.
#     msg.attach(part)
#     smtp = smtplib.SMTP_SSL(smtpHost, port)#需要一个安全的连接，用SSL的方式去登录得用SMTP_SSL，之前用的是SMTP（）.端口号465或587
#     smtp.login(sendAddr, password)#发送方的邮箱，和授权码（不是邮箱登录密码）
#     smtp.sendmail(sendAddr, recipientAddrs.split(";"), str(msg))#注意, 这里的收件方可以是多个邮箱,用";"分开, 也可以用其他符号
#     print("发送成功！")
#     smtp.quit()
#
# if __name__ == "__main__":
#     # try:
#         #设置好邮箱信息
#         smtpHost = 'smtp.qq.com'#这是QQ邮箱服务器。如果是腾讯企业邮箱，其服务器为smtp.exmail.qq.com。其他邮箱需要查询服务器地址和端口号。
#         port = 465 #端口号
#         sendAddr ='3048903923@qq.com'#发送方地址
#         password = input("gaqlontktiopdcgi")#手动输入授权码更安全.授权码的获取:打开qq邮箱->设置->账户->开启IMAP/SMTP服务->发送短信->授权码
#         recipientAddrs = '2656343994@qq.com;tingtign.yang@juneyaokc.com'#接收方可以是多个账户, 用分号分开,send_email()函数中手动设置
#         subject='python test from yangjian'#主题
#         content='Hello world'#正文内容
#         send_email(smtpHost, port, sendAddr, password, recipientAddrs, subject, content)#调用函数
#     # except:
#     #     print("Email send fail!")
