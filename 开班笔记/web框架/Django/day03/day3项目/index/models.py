from django.db import models


#声明自定义的objects,继承models.Manager
class AuthorManager(models.Manager):
    #添加自定义函数 -- 查询Author表中共有多少条数据
    def auCount(self):
        return self.all().count()

    #查询年龄小于指定年龄的作者信息
    def lt_age(self, age):
        return self.filter(age__lt=age) 


class BookManager(models.Manager):
    #添加函数，查询书名中包含指定关键字的书籍的信息
    def titleContains(self, keywords):
        return self.filter(title__contains=keywords)


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=10, verbose_name='出版社名')
    address = models.CharField(max_length=30, verbose_name='地址')
    city = models.CharField(max_length=10, verbose_name='所在城市')
    country = models.CharField(max_length=10, verbose_name='国家')
    website = models.URLField(verbose_name='网址')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publisher'
        verbose_name_plural = '出版社'


class Book(models.Model):
    #重新指定objects
    objects = BookManager()

    title = models.CharField(max_length=30, verbose_name='書名')
    publicate_date = models.DateField(verbose_name='出版時間')
    #增加一对多引用，引用自Publisher实体
    publisher = models.ForeignKey(Publisher, verbose_name='出版社', null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        verbose_name_plural = '书籍'
        ordering = ['-publicate_date']


class Author(models.Model):
    #使用AuthorManager覆盖当前的objects
    objects = AuthorManager()

    name = models.CharField(max_length=10, verbose_name='姓名')
    age = models.SmallIntegerField(verbose_name='年齡')
    email = models.EmailField(null=True, verbose_name='郵箱')
    #增加一个状态列，来表示用户是启用还是禁用，默认True表示启用
    isActive = models.BooleanField(default=True, verbose_name='激活狀態')

    #增加多对多引用，引用Book实体
    book = models.ManyToManyField(Book)

    #增加多对多引用，引用Publisher实体
    publisher = models.ManyToManyField(Publisher)

    def __str__(self):
        return self.name

    #声明内部类，来定义当前类在管理页面中的展现形式
    class Meta:
        #1.修改当前表名为 author
        db_table = 'author'
        #2.修改实体类在后台管理页中的名称（单数）
        verbose_name = '作者'
        #3.修改实体类在后台管理页中的名称（复数）
        verbose_name_plural = verbose_name
        #4.首先按年龄降序排序，再按id升序排序
        ordering = ['-age', 'id']


class Wife(models.Model):
    name = models.CharField(max_length=30, verbose_name='姓名')
    age = models.SmallIntegerField(verbose_name='年龄')
    #增加一对一的引用，引用自Author实体
    author = models.OneToOneField(Author, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wife'
        verbose_name = '夫人'
        verbose_name_plural = verbose_name