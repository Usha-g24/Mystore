from django.contrib import admin
from .product import Product
from .category import Category
from .customer import Customer

# Register your models here.
class Categoryinfo(admin.ModelAdmin):
    list_display = ['name']
class Productinfo(admin.ModelAdmin):
    list_display = ['name','category','prices']
class Customerinfo(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','password','mobile_number']

admin.site.register(Product,Productinfo)
admin.site.register(Category,Categoryinfo)
admin.site.register(Customer,Customerinfo)