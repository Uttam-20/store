from django.db import models

class Products(models.Model):
    proid=models.CharField(max_length=255,null=True)
    proname=models.CharField(max_length=255)
    quantity=models.IntegerField(null=True)
    pimg=models.ImageField(upload_to='images/',null=True)
    plink=models.CharField(max_length=300,null=True)
    price=models.CharField(max_length=255,null=True)
class Customers(models.Model):
    customerid=models.CharField(max_length=255)
    customerName=models.CharField(max_length=255)
    customerorder=models.CharField(max_length=255)
class Orders(models.Model):
    custid=models.CharField(max_length=255,null=True)
    oid=models.CharField(max_length=255)
    oname=models.CharField(max_length=255,null=True)
    quantity=models.IntegerField()
class Cart(models.Model):
    cid=models.CharField(max_length=255)
    proid=models.CharField(max_length=255)
    proname=models.CharField(max_length=255,null=True)
    quantity=models.IntegerField()