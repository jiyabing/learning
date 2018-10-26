from django import forms
from .models import *

class LoginForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['手机号码', '用户密码']
        labels = {
            '手机号码':'手机号',
            '用户密码':'密码',
        }
        widgets = {
            '手机号码':forms.TextInput(
                    attrs={
                        'max_length':11,
                        'class':'form-control',
                    }
            ),
            '用户密码':forms.PasswordInput(
                    attrs={
                        'max_length':20,
                        'min_length':6,
                        'placeholder':'请输入6-20位号码字符',
                        'class':'form-control',
                    }
            ),
        }