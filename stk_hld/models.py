from django.db import models

# Create your models here.
class StakeHolder(models.Model):
    stk_loginid=models.CharField(max_length=40)
    stk_password=models.CharField(max_length=40)
    stk_name=models.CharField(max_length=100)
    stk_email=models.CharField(max_length=40)
    stk_contact=models.CharField(max_length=40)
