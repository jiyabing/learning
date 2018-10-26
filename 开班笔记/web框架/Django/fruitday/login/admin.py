from django.contrib import admin
from .models import *

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ['用户昵称', '手机号码', '用户密码', '电子邮箱']
    list_editable = ['手机号码', '用户密码', '电子邮箱']


admin.site.register(Users, UsersAdmin)