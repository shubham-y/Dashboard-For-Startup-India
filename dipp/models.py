from django.db import models
from django.utils.timezone import now
from dept.models import DeptOfficer
# Create your models here.

class DippOfficer(models.Model):
    dipp_loginid=models.CharField(max_length=40)
    dipp_password=models.CharField(max_length=40)
    dipp_email=models.CharField(max_length=40)
    dipp_contact=models.CharField(max_length=40)

class Monitoring_Meeting(models.Model):
    meeting_date=models.DateField()
    subject=models.CharField(max_length=40)
    meeting_time=models.TimeField()
    upload_minute=models.FileField(null=True,blank=True,default='not uploaded')
    description=models.TextField(max_length=400,default='')


class Meeting(models.Model):
    meeting_date=models.DateField()
    subject=models.CharField(max_length=40)
    with_whom=models.ForeignKey(DeptOfficer,on_delete=models.CASCADE)
    meeting_time=models.TimeField()
    upload_minute=models.FileField(null=True,blank=True,default='not uploaded')
    description=models.TextField(max_length=400,default='')

class StatusReport(models.Model):
    date_of_upload = models.DateField(default=now )
    month=models.CharField(max_length=40)
    upload_statusreport=models.FileField(null=True,blank=True,default='not uploaded')


class ActionPoints(models.Model):
    action_no=models.CharField(max_length=2,primary_key=True,default='NULL')
    action_name=models.CharField(max_length=100,default='NULL')
    action_objective=models.CharField(max_length=200,default='NULL')
    action_description=models.CharField(max_length=500,default='NULL')
    update_time=models.DateField(default=now)


class Notify(models.Model):
    when= models.DateField(default=now )
    subject=models.CharField(max_length=40,default='NULL')
    type=models.CharField(max_length=40)
    desc=models.CharField(max_length=400)
    department=models.CharField(max_length=40)#who notifies
    actionpoint_no=models.ForeignKey(ActionPoints,on_delete=models.CASCADE,default='NULL')


class Target(models.Model):
    department=models.ForeignKey(DeptOfficer,on_delete=models.CASCADE)
    date_of_assignment=models.DateField(default=now )
    end_date=models.DateField()
    status=models.CharField(max_length=10,default='0')
    desc_of_target=models.CharField(max_length=400)
    report=models.CharField(max_length=400,default='not updated yet')
    actionpoint_no=models.ForeignKey(ActionPoints,on_delete=models.CASCADE)
