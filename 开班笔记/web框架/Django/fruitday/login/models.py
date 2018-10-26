from django.db import models

# Create your models here.
class Users(models.Model):
    手机号码 = models.CharField(max_length=11)
    用户密码 = models.CharField(max_length=20)
    用户昵称 = models.CharField(max_length=20)
    电子邮箱 = models.EmailField(null=True)
    激活状态 = models.BooleanField(default=True)

    def __str__(self):
        return self.用户昵称

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name