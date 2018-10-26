from celery import task
from dailyfresh import settings
from django.core.mail import send_mail


def send_register_active_email(to_email, username, token):
    """发送激活邮件"""
    # 组织邮件内容
    subject = '天天生鲜欢迎信息'
    message = ''
    sender = settings.EMAIL_HOST_USER
    receiver = [to_email]
    html_message = """
    <h1>%s, 欢迎您成为天天生鲜注册会员</h1>
    请点击以下链接激活您的账户<br/>
    <a href="http://127.0.0.1:8000/user/active/?token=%s">http://127.0.0.1:8000/user/active/</a>
    """ % (username, token)

    # 发送激活邮件
    # send_mail(subject=邮件标题, message=邮件正文,from_email=发件人, recipient_list=收件人列表)
    send_mail(subject, message, sender, receiver, html_message=html_message)
