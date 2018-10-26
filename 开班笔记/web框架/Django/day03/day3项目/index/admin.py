from django.contrib import admin
from .models import *

#声明高级管理类
class AuthorAdmin(admin.ModelAdmin):
    #1.指定在列表页中显示的字段们
    list_display = ['name', 'age', 'email']
    #2.指定能够链接到详情页的字段们
    list_display_links = ['name', 'email']
    #3.指定在列表页中就允许被编辑的字段们
    list_editable = ['age']
    #4.添加允许被搜索的字段们
    search_fields = ['name', 'email']
    #5.增加右侧过滤器，实现快速筛选
    list_filter = ['name', 'email']
    #6.指定在详情页中显示的字段们以及排序排列的顺序
    # fields = ['email', 'name', 'age', 'isActive']
    #7.指定字段的分组
    # fieldsets = [
    #     #分组1
    #     (
    #         '基本信息', {
    #             'fields': ('name', 'email'),
    #         }
    #     ),
    #     #分组2
    #     (
    #         '可选信息', {
    #             'fields': ('age', 'isActive'),
    #             'classes': ('collapse',),
    #         }
    #     ),
    # ]


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'publicate_date']
    #1.增加时间过滤器
    date_hierarchy = 'publicate_date'


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'website']
    list_editable = ['address', 'city']
    list_filter = ['address', 'city']
    fieldsets = [
        (
            '基本信息', {
                'fields': ('name', 'address', 'city'),
            }
        ),
        (
            '可选信息', {
                'fields': ('country', 'website'),
                'classes': ('collapse',),
            }
        ),
    ]

# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Wife)
