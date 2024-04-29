from django.contrib import admin
from .models import Product,Compnay


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name' , 'price' , 'description')

admin.site.register(Product,ProductAdmin)
admin.site.register(Compnay)
# Register your models here.


