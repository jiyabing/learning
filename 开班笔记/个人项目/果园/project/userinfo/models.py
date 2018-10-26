from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField('用户名', max_length=30, db_column='name', null=False)
    password = models.CharField('密码', max_length=20, db_column='password', null=False)
    phone = models.CharField('手机号码', max_length=11, db_column='phone', null=False)
    email = models.CharField('电子邮箱', max_length=40, db_column='email', null=False)
    create_time = models.DateTimeField('注册时间', auto_now=True)
    is_ban = models.BooleanField('禁用', default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'UserInfo'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Address(models.Model):
    name = models.CharField('收货人', max_length=30, db_column='name', null=False)
    address = models.CharField('地址', max_length=150, db_column='address', null=False)
    phone = models.CharField('手机号码', max_length=11, db_column='phone', null=False)
    user = models.ForeignKey(UserInfo)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Address'
        verbose_name = '收货地址'
        verbose_name_plural = verbose_name
