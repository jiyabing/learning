from django import forms
from .models import *

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['uphone', 'upwd']
        labels = {
            'uphone':'手机号',
            'upwd':'密码',
        }
        widget = {
            'uphone':forms.TextInput(
                    attrs={
                        'max_length':11,
                        'class':'form-control',
                    }
                ),
            'upwd':forms.PasswordInput(
                    attrs={
                        'max_length':20,
                        'placeholder':'请输入6-20位号码字符'
                        'class':'form-control',
                    }
                ),
        }