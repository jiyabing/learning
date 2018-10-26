from django.db import models

# Create your models here.
class Users(models.Model):
    uphone = models.CharField(max_length=11)
    upwd = models.CharField(max_length=20)
    uemail = models.EmailField(null=True)
    uname = models.CharField(max_length=20)
    isActive = models.BooleanField(default=True)