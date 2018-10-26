from django.db import models
from userinfo.models import UserInfo
from memberapp.models import Goods

# Create your models here.


class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo, db_column='user_id', on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, db_column='good_id', on_delete=models.CASCADE)
    count = models.IntegerField('数量', db_column='good_count')

    def __str__(self):
        return self.user.name

    class Meta:
        db_table = 'CartInfo'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name


STATUS = (
    (1, '未支付'),
    (2, '已支付'),
    (3, '订单取消')
)


class Order(models.Model):
    user = models.ForeignKey(UserInfo, db_column='user_id', on_delete=models.CASCADE)
    orderNo = models.CharField('订单号', max_length=100, null=False)
    order_time = models.DateTimeField('订单时间', auto_now=True)
    ads_name = models.CharField('收货人', max_length=30)
    ads_phone = models.CharField('联系电话', max_length=11, null=False)
    ads = models.CharField('地址', max_length=150, null=False)
    total = models.IntegerField('总数量')
    total_price = models.DecimalField('总价格', max_digits=8, decimal_places=2)
    order_detail = models.TextField('订单详情', null=True, blank=True)
    order_status = models.IntegerField('订单状态', choices=STATUS, default=1)

    def __unicode__(self):
        return self.user

    def get_order_status(self):
        if self.order_status == 1:
            return u'未支付'
        if self.order_status == 2:
            return u'已支付'
        if self.order_status == 3:
            return u'订单取消'
        else:
            return ''

    class Meta:
        db_table = 'Order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name
