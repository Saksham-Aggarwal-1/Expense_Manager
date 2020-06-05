from django.db import models

class User(models.Model):
    User_Id=models.IntegerField(primary_key=True)
    Username=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
    Currency=models.CharField(max_length=30)
class Transaction(models.Model):
    Transaction_Id=models.IntegerField(primary_key=True)
    Amount=models.FloatField()
    Date=models.DateField()
    Type=models.CharField(max_length=30)
    Frequency=models.IntegerField()
    Category=models.ForeignKey(Category)
    User=models.ForeignKey(User)
class Category(models.Model):
    Category_Id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=30)
    Budget=models.FloatField()
        



# Create your models here.
