from django.db import models
from datetime import datetime
# Create your models here.
class Employee(models.Model):
    Empno=models.IntegerField()
    Ename=models.CharField(max_length=255)
    sal=models.FloatField()
    job=models.CharField(max_length=100)
    
     
class Book(models.Model):
    number=models.IntegerField()
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    published_date=models.DateTimeField(default=datetime.now)