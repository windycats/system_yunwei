import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from selenium import webdriver
import os


class Email_send:
    def __init__(self, sender, receiver, name, psd, url):  # sender='2050645108@qq.com'  receiver='1306015138@qq.com'
        self.sender = sender  # 初始化发送者
        self.receiver = receiver  # 初始化接收者
        self.name = name  # 初始话用户
        self.psd = psd  # 初始话密码
        self.url = url  # 初始化url
        self.wd = webdriver.Chrome(executable_path=r"./chromedriver.exe")

    def send_emailqq(self):
        self.shootscreen()
        mail_server = 'smtp.qq.com'  # 邮箱服务端url
        sende = self.sender  # 发件人
        AuthCode = 'ngbzbcjjumpmbcbh'  # 邮箱发件授权码
        receive = self.receiver  # 收件人邮箱
        email = MIMEMultipart()
        email['Subject'] = '明途系统日常维护'  # 邮件主题
        email['From'] = Header('自动化组件', 'utf-8')
        email['TO'] = Header('minto_system', 'utf-8')
        att1 = MIMEBase('application', 'octet-stream')
        att1.set_payload(open(r'img/1.png', 'rb').read())  # 文件读取路径
        att1.add_header('Content-Disposition', 'attachment', filename=Header('登录截图.png', 'gbk').encode())
        encoders.encode_base64(att1)
        email.attach(att1)  # 执行附件添加

        email.attach(MIMEText('明途系统日常运维', 'plain', 'utf-8'))
        # 发送邮件
        # 连接服务器
        smtp_connect = smtplib.SMTP_SSL(mail_server, port=465)
        # 验证身份，进行授权
        smtp_connect.login(sende, AuthCode)
        # 发送邮件
        smtp_connect.sendmail(sende, receive, email.as_string())
        smtp_connect.quit()

    def login(self):
        self.wd.get(self.url)  # 获取网页
        self.wd.maximize_window()  # 最大化窗口
        self.wd.implicitly_wait(5)  # 等待5s
        self.wd.find_element_by_xpath('//*[@id="u34_input"]').send_keys(self.name)  # 账号
        self.wd.find_element_by_xpath('//*[@id="u35_input"]').send_keys(self.psd)  # 密码
        self.wd.find_element_by_xpath('//*[@id="loginBut"]').click()

    def shootscreen(self):
        try:
            self.login()
            self.wd.find_element_by_xpath('//div[contains(text(),"我的待办")]')
        except:
            pass
        self.wd.get_screenshot_as_file(
            r'img/1.png')  # 操作登陆后后截图存留
        self.wd.quit()


# loginsystem = Login('http://172.16.0.134:9012/minto/home', 'gongzy', '123456')
# loginsystem.shootscreen()
# input('程序执行成功，按任意键退出：')

if __name__ == '__main__':
    excute = Email_send('2050645108@qq.com',
                        '1306015138@qq.com', 'yangd', '123456', 'http://172.16.0.134:9012/minto/home')  # 实例化用户
    # 依次是发件人，收件人，用户，密码，域名
    excute.send_emailqq()  # 执行截图
