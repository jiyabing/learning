from django.db import models

# Create your models here.
class GoodsType(models.Model):
    title = models.CharField(max_length=20, verbose_name='类型')
    picture = models.ImageField(upload_to='static/upload/goodstype', verbose_name='图片')
    desc = models.TextField(verbose_name='商品类型描述', null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'goodstype'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name


class Goods(models.Model):
    name = models.CharField(max_length=50, verbose_name='名称')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='价格')
    spec = models.CharField(max_length=30, verbose_name='规格')
    picture = models.ImageField(upload_to='static/upload/goods', verbose_name='商品图片')
    isActive = models.BooleanField(default=True, verbose_name='激活状态')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'goods'
        verbose_name = '商品名称'
        verbose_name_plural = verbose_name

    #增加对GoodsType的引用（一对多）
    goodsType = models.ForeignKey(GoodsType, null=True)