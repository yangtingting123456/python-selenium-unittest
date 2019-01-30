import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart

sender = '3048903923@qq.com'  # 发件人邮箱
password = 'gaqlontktiopdcgi'  # 发件人邮箱密码
addressed_eamil = 'tingting.yang@juneyaokc.com'  # 收件人邮箱

class Send_Email():

    def mail():
        try:
            # 创建一个带附件的实例
            message = MIMEMultipart()
            message['From'] = formataddr(['一曲离殇', sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            message['To'] = formataddr(['杨婷婷', addressed_eamil])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            message['Subject'] = "sish自动化测试报告"  # 邮件的主题，也可以说是标题

            # 邮件正文内容
            message.attach(MIMEText('\n    你好！下面是本次运行sish自动化测试的测试报告，附件1是本次的测试报告，附件2是本次的bug列表，请注意查收，'
                                    '如果已经查收，不用回复，谢谢，祝你生活愉快！' + "  \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n杨婷婷  技术研发部 | 测试工程师  " + "\n上海均瑶科创信息技术有限公司"
                                    + "\nPhone: 17633710286 |Email:tingting.yang@juneyaokc.com" + "\nAdd: 上海市徐汇区肇嘉浜路789号(均瑶国际广场)3层E单元",
                                    'plain', 'utf-8'))

            # 构造附件1
            att1 = MIMEText(open('‪D:\result\result.html', 'rb').read(), 'base64', 'utf-8')

            att1["Content-Type"] = 'application/octet-stream'
            # filename是附件名，附件名称为中文时的写法
            att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", "测试.txt"))
            message.attach(att1)

            # 构造附件2
            att2 = MIMEText(open('‪D:\result\result.html', 'rb').read(), 'base64', 'utf-8')
            att2["Content-Type"] = 'application/octet-stream'
            # 附件名称非中文时的写法
            att2["Content-Disposition"] = 'attachment; filename="test.txt")'
            message.attach(att2)

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，一般端口是25
            server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(sender, addressed_eamil, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:
            print("邮件发送失败")


if __name__ == '__main__':
    Send_Email()
