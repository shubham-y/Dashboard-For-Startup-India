from django.db import models
from django.utils.timezone import now

# Create your models here.
class DeptOfficer(models.Model):
    dept_loginid=models.CharField(max_length=40,primary_key=True)
    dept_password=models.CharField(max_length=40)
    dept_name=models.CharField(max_length=100)
    dept_email=models.CharField(max_length=40)
    dept_contact=models.CharField(max_length=40)

class Feedback(models.Model):
    stakeholder=models.CharField(max_length=40)
    dept_loginid=models.ForeignKey(DeptOfficer,on_delete=models.CASCADE,default=None)
    rating=models.CharField(max_length=40)
    date=models.DateField(default=now)
    dept=models.CharField(max_length=40)

class Ranking(models.Model):
    dept_loginid=models.ForeignKey(DeptOfficer,on_delete=models.CASCADE)
    score1=models.CharField(max_length=40,default='0')
    score2=models.CharField(max_length=40,default='0')
