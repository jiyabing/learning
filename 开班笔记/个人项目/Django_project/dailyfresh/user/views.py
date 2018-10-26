from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect
import re
from django.views.generic.base import View
from django_redis import get_redis_connection
from dailyfresh import settings
from django.urls import reverse
from celery_tasks import tasks
from goods.models import GoodsSKU
from order.models import OrderInfo, OrderGoods
from user.models import User, Address
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired


# Create your views here.
from utils.mixin import LoginRequiredMixin


def login_view(request):
    if request.method == 'GET':
        # 判断用户是否记住用户名
        username = request.COOKIES.get('username')
        checked = 'checked'
        if username is None:
            # 没有记住用户名
            username = ''
            checked = ''
        return render(request, 'login.html', {'username': username, 'checked': checked})

    if request.method == 'POST':
        # 1.接收参数
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        remember = request.POST.get('remember')

        # 2.参数校验（后端校验）
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '参数不完整'})

        # 3.业务处理：登录校验
        user = authenticate(username=username, password=password)
        if user is not None:
            # 用户名和密码正确
            if user.is_active:
                # 用户已激活
                # 记住用户的登录状态
                login(request, user)

                # 获取用户登录之前访问的url地址，默认跳转到首页
                next_url = request.GET.get('next', reverse('goods:index'))  # None
                # print(next_url)

                # 跳转到next_url
                response = redirect(next_url)  # HttpResponseRedirect

                # 跳转到首页
                # response = redirect(reverse('goods:index'))  # HttpResponseRedirect
                # 将用户名赋值给index
                # 方式1：直接在session里面记录该值，并传递给重定向
                # request.session['is_login'] = username
                # 方式2： 设置cookie，不安全
                # response.set_cookie('is_login', username)
                # 方式3：由于采用django自带的authenticate，因此，可以在模板中使用user.is_authenticated

                # 判断是否需要记住用户名
                if remember == 'on':
                    # 设置cookie username
                    response.set_cookie('username', username, max_age=7 * 24 * 3600)
                else:
                    # 删除cookie username
                    response.delete_cookie('username')
                # 跳转到首页
                return response
            else:
                # 用户未激活
                return render(request, 'login.html', {'errmsg': '用户未激活'})
        else:
            # 用户名或密码错误
            return render(request, 'login.html', {'errmsg': '用户名或密码错误'})


def logout_view(request):
    """退出"""
    # 清除用户登录状态,内置的logout函数会自动清除当前session
    logout(request)

    # 跳转到登录
    return redirect(reverse('user:login'))


def register_view(request):
    if request.method == 'POST':
        # 1.接收参数
        username = request.POST.get('user_name')
        password1 = request.POST.get('pwd')
        password2 = request.POST.get('cpwd')
        email = request.POST.get('email')

        # 2.参数校验(后端校验)
        # 检测数据的完整性
        if not all([username, password1, email]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})

        # 校验用户名是否已注册
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user:
            return render(request, 'register.html', {'errmsg': '用户名已注册'})

        # 判断两次输入的密码是否一致
        if password1 != password2:
            return render(request, 'register.html', {'errmsg': '两次密码不一致'})

        # 校验邮箱格式
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})

        # 校验邮箱是否已注册
        try:
            result = User.objects.get(email=email)
        except User.DoesNotExist:
            result = None
        if result:
            return render(request, 'register.html', {'errmsg': '邮箱已注册'})

        # 3.业务处理：注册
        new_user = User.objects.create_user(username, email, password1)
        new_user.is_active = 0
        new_user.save()

        # 注册之后，需要给用户的注册邮箱发送激活邮件，在激活邮件中需要包含激活链接
        # 激活链接: /user/active/用户id
        # 存在问题: 其他用户恶意请求网站进行用户激活操作
        # 解决问题: 对用户的信息进行加密，把加密后的信息放在激活链接中，激活的时候在进行解密
        # /user/active/加密后token信息

        # 对用户身份信息进行加密，生成激活的token信息
        serializer = Serializer(settings.SECRET_KEY, 3600*7)
        info = {'confirm': new_user.id}
        # 返回bytes类型
        token = serializer.dumps(info)
        # str
        token = token.decode()

        # 发送激活邮件
        tasks.send_register_active_email.delay(email, username, token)

        # 跳转到登录页
        return redirect(reverse('user:login'))

    return render(request, 'register.html')


def active_view(request):
    """激活"""
    serializer = Serializer(settings.SECRET_KEY, 3600 * 7)
    token = request.GET.get('token')
    try:
        # 解密
        info = serializer.loads(token)
        # 获取待激活用户id
        user_id = info['confirm']
        # 激活用户
        user = User.objects.get(id=user_id)
        user.is_active = 1
        user.save()

        # 跳转登录页面
        return redirect(reverse('user:login'))
    except SignatureExpired as e:
        # 激活链接已失效
        # 实际开发: 返回页面，让你点击链接再发激活邮件
        return HttpResponse('激活链接已失效')


# /user/
# class UserInfoView(View):
# class UserInfoView(LoginRequiredView):
class UserInfoView(LoginRequiredMixin, View):
    """用户中心-信息页"""

    def get(self, request):
        """显示"""
        # 获取登录用户
        user = request.user

        # 获取用户的默认收货地址
        address = Address.objects.get_default_address(user)

        # 获取用户的最近浏览商品的信息
        # 若采用redis第三包交互时
        # from redis import StrictRedis
        # conn = StrictRedis(host='172.16.179.142', port=6379, db=5)

        # 返回StrictRedis类的对象
        # 若采用django-redis包时
        conn = get_redis_connection('default')
        # 拼接key
        history_key = 'history_%d' % user.id

        # lrange(key, start, stop) 返回是列表
        # 获取用户最新浏览的5个商品的id
        sku_ids = conn.lrange(history_key, 0, 4)  # [1, 3, 5, 2]

        skus = []
        for sku_id in sku_ids:
            # 根据商品的id查询商品的信息
            sku = GoodsSKU.objects.get(id=sku_id)
            # 追加到skus列表中
            skus.append(sku)

        # 组织模板上下文
        context = {
            'address': address,
            'skus': skus,
            'page': 'user'
        }

        # 使用模板
        return render(request, 'user_center_info.html', context)


# /user/order
# class UserOrderView(View):
# class UserOrderView(LoginRequiredView):
class UserOrderView(LoginRequiredMixin, View):
    """用户中心-订单页"""

    def get(self, request, page):
        """显示"""
        # 获取登录用户
        user = request.user
        # 查询所有订单
        info_msg = 1   # 若有订单则为1
        try:
            order_infos = OrderInfo.objects.filter(user=user).order_by('-create_time')
        except OrderInfo.DoesNotExist:
            info_msg = 0

        if len(order_infos) == 0:
            info_msg = 0
        context = {
            'page': 'order',
            'info_msg': info_msg,
        }
        if info_msg == 1:

            for order_info in order_infos:
                order_goods = OrderGoods.objects.filter(order=order_info)
                for order_good in order_goods:
                    # 商品小计
                    amount = order_good.price * order_good.count
                    order_good.amount = amount
                order_info.order_goods = order_goods
                order_info.status_title = OrderInfo.ORDER_STATUS[order_info.order_status]
                # order_info.status = order_info.ORDER_STATUS_CHOICES[order_info.order_status-1][1]

            # 分页操作
            from django.core.paginator import Paginator
            paginator = Paginator(order_infos, 3)

            # 处理页码
            page = int(page)

            if page > paginator.num_pages:
                # 默认获取第1页的内容
                page = 1

            # 获取第page页内容, 返回Page类的实例对象
            order_infos_page = paginator.page(page)

            # 页码处理
            # 如果分页之后页码超过5页，最多在页面上只显示5个页码：当前页前2页，当前页，当前页后2页
            # 1) 分页页码小于5页，显示全部页码
            # 2）当前页属于1-3页，显示1-5页
            # 3) 当前页属于后3页，显示后5页
            # 4) 其他请求，显示当前页前2页，当前页，当前页后2页
            num_pages = paginator.num_pages
            if num_pages < 5:
                # 1-num_pages
                pages = range(1, num_pages + 1)
            elif page <= 3:
                pages = range(1, 6)
            elif num_pages - page <= 2:
                # num_pages-4, num_pages
                pages = range(num_pages - 4, num_pages + 1)
            else:
                # page-2, page+2
                pages = range(page - 2, page + 3)

            context = {
                'page': 'order',
                'order_infos': order_infos,
                'info_msg': info_msg,
                'pages' : pages,
                'order_infos_page': order_infos_page
            }
        return render(request, 'user_center_order.html', context)


# /user/address
# class AddressView(View):
# class AddressView(LoginRequiredView):
class AddressView(LoginRequiredMixin, View):
    """用户中心-地址页"""
    def get(self, request):
        """显示"""
        # 获取登录用户user
        user = request.user
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     address = None

        default_address = Address.objects.get_default_address(user)

        all_address = Address.objects.get_all_address(user)

        # 组织模板上下文
        context = {
            'address': default_address,
            'have_address': all_address,
            'page': 'address'
        }

        # 使用模板
        return render(request, 'user_center_site.html', context)

    def post(self, request):
        """地址添加"""
        # 接收参数
        receiver = request.POST.get('receiver')
        addr = request.POST.get('direction')
        zip_code = request.POST.get('mail_code')
        phone = request.POST.get('phone_number')

        # 参数校验
        if not all([receiver, addr, phone]):
            return render(request, 'user_center_site.html', {'errmsg': '数据不完整'})

        # 校验手机号

        # 业务处理：添加收货地址
        # 如果用户已经有默认地址，新添加的地址作为非默认地址，否则作为默认地址
        # 获取登录用户user
        user = request.user
        # try:
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     address = None

        address = Address.objects.get_default_address(user)

        is_default = True
        if address is not None:
            is_default = False

        # 添加收货地址
        Address.objects.create(user=user,
                               receiver=receiver,
                               addr=addr,
                               zip_code=zip_code,
                               phone=phone,
                               is_default=is_default)

        # 返回应答，刷新地址页面
        return redirect(reverse('user:address'))
