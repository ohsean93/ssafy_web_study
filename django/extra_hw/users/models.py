from django.db import models

# Create your models here.
# id,first_name,last_name,age,country,phone,balance
class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    balance = models.IntegerField()
