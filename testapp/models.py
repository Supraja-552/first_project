from django.db import models

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    salary=models.FloatField()
    eaddress=models.CharField(max_length=30)
class Company(models.Models):
    cname=models.CharField(max_length=100)
    clocation=models.CharField(max_length=100)
    cid=models.IntegerFiels()
    no_of_employees=models.IntegerField()
