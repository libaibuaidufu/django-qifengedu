import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name=u"昵称")
    mobile = models.CharField(max_length=11, verbose_name="手机号码")
    birday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(max_length=50, choices=(("male", "男"), ("female", "女")), default="female")
    address = models.CharField(max_length=100, default="")
    image = models.ImageField(max_length=200, upload_to="image/%Y/%m")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    code = models.CharField(max_length=20, verbose_name="验证码")
    send_type = models.CharField(max_length=30, verbose_name="验证码类型",
                                 choices=(("register", "注册"), ("forget", "找回密码"), ("update_email", "修改邮箱")))

    send_time = models.DateField(default=datetime.datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{0}({1})".format(self.code, self.email)
