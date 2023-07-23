from django.contrib import admin
from .models import Member
from .model2 import Products
from .model2 import Customers
from .model2 import Orders
from .model2 import Cart
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("memid","name", "password","mobile","address")
admin.site.register(Member,MemberAdmin)
class ProductsAdmin(admin.ModelAdmin):
    list_display=("proid","proname","pimg","quantity","price")
admin.site.register(Products,ProductsAdmin)
class CustomersAdmin(admin.ModelAdmin):
    list_display=("customerid","customerName","customerorder")
admin.site.register(Customers,CustomersAdmin)
class CartAdmin(admin.ModelAdmin):
    list_display=("cid","proid","quantity")
admin.site.register(Cart,CartAdmin)
class OrdersAdmin(admin.ModelAdmin):
    list_display=("custid","oid","oname","quantity")
admin.site.register(Orders,OrdersAdmin)
