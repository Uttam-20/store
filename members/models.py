from django.db import models

class Member(models.Model):
    memid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255,null=True)
    address=models.CharField(max_length=255,null=True)


