# coding:utf-8
__author__ = "dfk"
__date__ = "2018/2/10 11:46"

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from onlineedu.settings import EMAIL_FROM


# 随机字符串
def random_str(randomlength=8):
    str = ""
    chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_type_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    email_record.email = email
    code = random_str(16)
    email_record.code = code
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == 'register':
        email_title = "豆腐块教育网注册激活链接"
        email_body = "请点击下面的链接激活账户: http://127.0.0.1:8000/active/{code}".format(code=code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
