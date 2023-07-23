from django.urls import path
from . import views

urlpatterns=[
    path('',views.members,name="members"),
    path('home',views.home,name="home"),
    path('sign',views.sign,name="sign"),
    path('login',views.login,name="login"),
    path('log',views.log,name="log"),
    path('products/',views.products,name="products"),
    path('products/show/customers/',views.customer,name="customer"),
    path('myorders/',views.myorders,name="myorders"),
    path('products/show/addcart/',views.cart,name="addcart"),
    path('products/show/',views.show,name="show"),
    path('cart/',views.showcart,name="showcart"),
    path('account/',views.account,name="account"),
    path('logout/',views.logout,name="logout"),
]