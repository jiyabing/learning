from django.db import models

# Create your models here.


class GoodType(models.Model):
    title = models.CharField('商品类型', max_length=20, default='无')
    desc = models.CharField('类别描述', max_length=300, default='类别描述')
    flag = models.IntegerField(default=0)
    is_delete = models.BooleanField('删除', default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'GoodType'
        verbose_name = '商品类型'
        verbose_name_plural = verbose_name


class Goods(models.Model):
    title = models.CharField('商品名称', max_length=30, null=False)
    price = models.DecimalField('商品价格', max_digits=8, decimal_places=2)
    picture = models.ImageField('商品图片', upload_to='static/image/goods', default='normal.png')
    desc = models.CharField('商品描述', max_length=200)
    is_delete = models.BooleanField('下架', default=False)
    type = models.ForeignKey(GoodType)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Goods'
        verbose_name = '商品'
        verbose_name_plural = verbose_name
