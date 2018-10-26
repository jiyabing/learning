from django.contrib import admin
from .models import *

# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'spec']
    list_editable = ['price', 'spec']


admin.site.register(GoodsType)
admin.site.register(Goods, GoodsAdmin)