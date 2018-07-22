from email import encoders
import os
import traceback
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
 
 
# 中文处理
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
 
def send_email(to_addr_in,filepath_in):
    # 邮件发送和接收人配置
    from_addr = '18829897162@163.com'
    smtp_server = 'smtp.163.com'
    password = '18829897162ly'  #这是你邮箱的第三方授权客户端密码，并非你的登录密码
    to_addr = to_addr_in
    to_addrs = to_addr.split(',')
	

    #msg = MIMEText('你好！这里是智能家居物联网服务平台。','plain','utf-8')
    msg = MIMEText('<html><body><h1>智能家居物联网服务平台</h1>' +
                   '<p>你好！这里是智能家居物联网服务平台<a href="http://47.95.254.34:8512/">平台入口</a>...</p>' +
                   '</body></html>', 'html', 'utf-8')
    msg['From'] = _format_addr('ATM-邮件助手 <%s>' % from_addr)        # 显示的发件人
    msg['To'] = ",".join(to_addrs)                                    # 多个显示的收件人
    msg['Subject'] = Header('智能家居物联网服务平台', 'utf-8').encode()      # 显示的邮件标题
 
    try:
        server = smtplib.SMTP(smtp_server, 25)
        # server.starttls()
        server.set_debuglevel(1)  # 用于显示邮件发送的执行步骤
        server.login(from_addr, password)
        # print to_addrs
        server.sendmail(from_addr, to_addrs, msg.as_string())
        server.quit()
    except Exception:
        print("Error: unable to send email")
        print(traceback.format_exc())
 
if __name__ == '__main__':
    send_email('2275349027@qq.com,ofo18829897162@gmail.com','/home/orchid/pro/tools/	')
