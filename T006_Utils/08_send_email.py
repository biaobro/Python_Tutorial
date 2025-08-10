# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : 08_send_email.py
@Project            : T006_Utils
@CreateTime         : 2025/8/10 11:23
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2025/8/10 11:23 
@Version            : 1.0
@Description        : None
"""

import smtplib
from email.mime.text import MIMEText


def send_email(sender_email, sender_password, receiver_email, subject, message, smtp_server='smtp.163.com',
               smtp_port=25):
    """发送邮件 (需要配置SMTP服务器)."""
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # 启用 TLS 加密
        server.login(sender_email, sender_password)  # 登录邮箱
        server.sendmail(sender_email, [receiver_email], msg.as_string())
        server.quit()
        return "邮件发送成功"
    except Exception as e:
        return f"邮件发送失败: {e}"


#  **请注意:**  出于安全考虑，不要在代码中硬编码您的邮箱密码。
#  示例 (请替换为您的邮箱信息和目标邮箱)
sender = "biaobro@163.com"

# 这里需要特别注意，password 不是邮箱登录密码，而是授权码
password = "FPgikEkMsXSBk3EK"
receiver = "biaobro@sina.com"
email_result = send_email(sender, password, receiver, "测试邮件", "这是一封测试邮件。")
print(email_result)
