from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from dipp.models import Monitoring_Meeting,Meeting,StatusReport,Notify,Target,ActionPoints,DippOfficer,Dept_action_points
from dept.models import DeptOfficer,Ranking
from stk_hld.models import StakeHolder
from django.core.mail import send_mail
from django.utils import timezone
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.db.models import Count
from django.db.models import Q
from django.db.models import Max
from dept.fusioncharts import FusionCharts
from collections import OrderedDict
import simplejson as json
from datetime import date
from dateutil.relativedelta import relativedelta
# Create your views here.

#def dipp_home(request):
#    if 'username' not in request.session:
#        return HttpResponseRedirect(reverse('login'))
#    else:
#        return render(request,'dipp/home.html')

def dipp_home(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        userid=request.session['username']
        print(userid)
        main=[]
        a=ActionPoints.objects.all()
        for i in range(1,len(a)+1):

            d=DeptOfficer.objects.all().distinct()
            print(d)
            l=[]
            for dept in d:
                print(dept.dept_loginid)
                Target_assigned=(Target.objects.filter(department_id=dept.dept_loginid,actionpoint_no_id=i))
                Target_completed=(Target.objects.filter(department_id=dept.dept_loginid,actionpoint_no_id=i,status='1'))
                
                l.append([dept.dept_name,Target_assigned,Target_completed])
                #count = Count(dept.department_id,filter=Q(actionpoint_no_id=1))
                #print(count)

            main.append(l)
        print(main)
        ap=ActionPoints.objects.all()
        j=[]
        k=[]
        d=0
        for i in range(0,len(ap)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        m=zip(ap,j,k)

        main=zip(main,ap,j,k)
        r=Ranking.objects.all()
        max=Ranking.objects.all().aggregate(Max('score1'))
        max=int(max['score1__max'])
        print(max)
        print(type(max))
        #print(max['score1__max'])
        print(r)
        '''for i in r:
            print(i.score1)'''
        l=[]
        if max!=0:
            for i in r:
                
                d=DeptOfficer.objects.get(dept_loginid=i.dept_loginid.dept_loginid)
                print(d)
                score2=float(i.score2)*10
                score1=(float(i.score1)/max)*50
                total=score1+score2
                l.append([d.dept_name,total])
                l.sort(key=lambda x: x[1],reverse=True)
                l=l[0:3]
                print(l)
                for  m,val,j,k in main:
                    print(m)
        return render(request,'dipp/home.html',{'ap':m,'d':d,'main':main,'userid':userid,'l':l})


def add_dept(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        a=ActionPoints.objects.all()
        return render(request,'dipp/add_dept.html',{'actionpoints':a})

def add_sh(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request,'dipp/add_sh.html')

def add_dept_action_new(request):
    actionpoint_no = request.POST.getlist('actionpoint','NULL')
    print(actionpoint_no)
    return HttpResponseRedirect(reverse('add_dept'))

def add_dept_action(request):
    dept_name=request.POST.get('dept_name','NULL')
    actionpoint_no = request.POST.getlist('actionpoint','NULL')
    email=request.POST.get('email','NULL')
    contact=request.POST.get('contact','NULL')
    dept_id=request.POST.get('dept_id','NULL')
    dept_id='dept_'+dept_id
    dept_password=request.POST.get('dept_password','NULL')
    l=DeptOfficer.objects.filter(dept_name=dept_name)
    i=DeptOfficer.objects.filter(dept_loginid=dept_id)

    if len(i)>=1:
        return HttpResponse('ID is already used')
    if len(l)==1:
        DeptOfficer.objects.filter(dept_name=dept_name).update(dept_email=email,dept_loginid=dept_id,dept_password=dept_password)
        subject = 'Department head for startup India'
        message = 'You will be looking after and updating about progress of'+ dept_name +'to us\nyour userid :' + dept_id +'\n your password : '+ dept_password +'.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        # print('working')
        send_mail( subject, message, email_from, recipient_list , fail_silently=True)
        return HttpResponseRedirect(reverse('add_dept'))

    else:
        s=DeptOfficer(dept_loginid=dept_id,dept_email=email,dept_contact=contact,dept_password=dept_password,dept_name=dept_name)
        s.save()
        for actionpoint in actionpoint_no:
            a=Dept_action_points(department_id=dept_id,actionpoint_no_id=actionpoint)
            a.save()
        
        

        if s.dept_loginid:
            r=Ranking(dept_loginid=s,score1='0',score2='0')
            r.save()
            subject = 'Department head for startup India'
            message = 'You will be looking after and updating about progress of'+ dept_name +'to us\nyour userid :' + dept_id +'\n your password : '+ dept_password +'.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            #print('working')
            send_mail( subject, message, email_from, recipient_list , fail_silently=True)
            return HttpResponseRedirect(reverse('add_dept'))

def add_sh_action(request):
    sh_name=request.POST.get('sh_name','NULL')
    email=request.POST.get('email','NULL')
    contact=request.POST.get('contact','NULL')
    sh_id=request.POST.get('sh_id','NULL')
    sh_id='sh_'+sh_id
    sh_password=request.POST.get('sh_password','NULL')
    i=StakeHolder.objects.filter(stk_loginid=sh_id)
    if len(i)>=1:
        return HttpResponse('ID is already used')
    else:
        s=StakeHolder(stk_loginid=sh_id,stk_email=email,stk_contact=contact,stk_password=sh_password,stk_name=sh_name)
        s.save()
        if s.id:
            subject = 'StakeHolder for startup India'
            message = 'Welcome StakeHolder '+ sh_name +'!!\n You will now be able to see all updates of startup India \nyour userid :' + sh_id +'\n your password : '+ sh_password +'.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            print('working')
            send_mail( subject, message, email_from, recipient_list , fail_silently=True)
            return HttpResponseRedirect(reverse('add_sh'))

def add_monitory_meeting(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        m = datetime.now().strftime("%Y-%m-%d")
        return render(request,'dipp/add_monitory_meeting.html',{'m':m})


def add_monitory_meeting_action(request):
    m_date=request.POST.get('m_date','NULL')
    m_time=request.POST.get('m_time','NULL')
    m_subject=request.POST.get('m_subject','NULL')
    desc=request.POST.get('desc','NULL')
    s=Monitoring_Meeting(meeting_date=m_date,meeting_time=m_time,subject=m_subject,description=desc)
    s.save()
    return HttpResponseRedirect(reverse('add_monitory_meeting'))


def view_upcoming_meetings_action(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        now = timezone.now()
        m=Monitoring_Meeting.objects.all().filter(meeting_date__gte= now).order_by('meeting_date')
        print(m)
        j=[]
        k=[]
        for i in range(0,len(m)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(m,j,k)

    return render(request,'dipp/upcoming_meetings.html',{'m':z})

def view_prev_meeting(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        n='not uploaded'
        now = timezone.now()
        m=Monitoring_Meeting.objects.all().filter(meeting_date__lte= now).order_by('-meeting_date')
    j=[]
    k=[]
    for i in range(0,len(m)):
        d='#id'+str(i)
        e='id'+str(i)
        j.append(d)
        k.append(e)
    z=zip(m,j,k)
    return render(request,'dipp/prev_meetings.html',{'m':z,'n':n})

def upload_minute(request,mid):
    myfile=request.POST.get('myfile','NULL')
    i=Monitoring_Meeting.objects.get(id=mid)
    print(i.id)
    uploadedfileurl=''
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploadedfileurl=fs.url(filename)
    i.upload_minute=uploadedfileurl
    i.save()
    now = timezone.now()
    n='not uploaded'
    m=Monitoring_Meeting.objects.all().filter(meeting_date__lte= now).order_by('-meeting_date')
    return HttpResponseRedirect(reverse('view_prev_meeting'))


def add_meeting(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        s=StakeHolder.objects.all()
        d=DeptOfficer.objects.all()
        date = datetime.now().strftime("%Y-%m-%d")
        return render(request,'dipp/add_meeting.html',{'s':s,'d':d,'date':date})

def add_meeting_action(request):
    m_date=request.POST.get('m_date','NULL')
    m_time=request.POST.get('m_time','NULL')
    m_subject=request.POST.get('m_subject','NULL')
    desc=request.POST.get('desc','NULL')
    with_whom=request.POST.get('with_whom','NULL')
    d=DeptOfficer.objects.get(dept_name=with_whom)
    m=Meeting(meeting_date=m_date,meeting_time=m_time,subject=m_subject,description=desc,with_whom=d)
    m.save()
    return HttpResponseRedirect(reverse('add_meeting'))

def view_upcoming_normalmeetings(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
        now = timezone.now()
    else:
        now = timezone.now()
        m=Meeting.objects.all().filter(meeting_date__gte= now).order_by('meeting_date')
        j=[]
        k=[]
        for i in range(0,len(m)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(m,j,k)
    return render(request,'dipp/upcoming_normalmeetings.html',{'m':z})


def view_prev_normalmeeting(request):
        if 'username' not in request.session:
            return HttpResponseRedirect(reverse('login'))
        else:
            n='not uploaded'
            now = timezone.now()
            m=Meeting.objects.all().filter(meeting_date__lte= now).order_by('-meeting_date')

        j=[]
        k=[]
        for i in range(0,len(m)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(m,j,k)
        return render(request,'dipp/prev_normalmeetings.html',{'m':z,'n':n})

def upload_normalmeeting_minute(request,mid):
    myfile=request.POST.get('myfile','NULL')
    i=Meeting.objects.get(id=mid)
    uploadedfileurl=''
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploadedfileurl=fs.url(filename)
    i.upload_minute=uploadedfileurl
    i.save()
    now = timezone.now()
    n='not uploaded'
    m=Meeting.objects.all().filter(meeting_date__lte= now).order_by('-meeting_date')
    return HttpResponseRedirect(reverse('view_prev_normalmeeting'))


def add_status_report(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request,'dipp/add_status_report.html')

def add_status_report_action(request):
    s_month=request.POST.get('s_month','NULL')
    myfile=request.POST.get('myfile','NULL')
    uploadedfileurl=''
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploadedfileurl=fs.url(filename)
    l=StatusReport.objects.filter(month=s_month)
    if len(l)>=1:
        i=StatusReport.objects.get(month=s_month)
        now = timezone.now()
        print(i.upload_statusreport)
        i.upload_statusreport=uploadedfileurl
        i.date_of_upload=now
        i.save()
        print(i.upload_statusreport)
    else:
        s=StatusReport(month=s_month,upload_statusreport=uploadedfileurl)
        s.save()
    return HttpResponseRedirect(reverse('add_status_report'))


def view_status_report(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
        now = timezone.now()
    else:
        #s=StatusReport.objects.all().filter(month__gte= now).order_by('meeting_date')
        s=StatusReport.objects.all().order_by('month')
    return render(request,'dipp/view_status_report.html',{'s':s})

def notify(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        ap=ActionPoints.objects.all()
        return render(request,'dipp/notify.html',{'a':ap})

def notify_action(request):
    n_type=request.POST.get('n_type','NULL')
    desc=request.POST.get('desc','NULL')
    subject=request.POST.get('subject','NULL')
    department='dipp'
    actionpoint=request.POST.get('actionpoint','NULL')

    s=Notify(desc=desc,type=n_type,department=department,subject=subject,actionpoint_no_id=actionpoint)
    s.save()
    return HttpResponseRedirect(reverse('notify'))

def view_notification(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))

    else:
        #s=StatusReport.objects.all().filter(month__gte= now).order_by('meeting_date')
        n=Notify.objects.all().order_by('when')
        return render(request,'dipp/view_notification.html',{'n':n})


def add_target(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        d=DeptOfficer.objects.all()
        a=ActionPoints.objects.all()
        date = datetime.now().strftime("%Y-%m-%d")
        return render(request,'dipp/add_target.html',{'d':d,'a':a,'date':date})

def add_target_action(request):
    department=request.POST.get('department','NULL')
    end_date=request.POST.get('m_date','NULL')
    date_of_assignment=datetime.now()
    target=request.POST.get('target','NULL')
    actionpoint=request.POST.get('actionpoint','NULL')
    d=DeptOfficer.objects.get(dept_loginid=department)

    t=Target(department=d,date_of_assignment=date_of_assignment,end_date=end_date,desc_of_target=target,actionpoint_no_id=actionpoint)
    t.save()
    return HttpResponseRedirect(reverse('add_target'))

def load_action(request):
    department=request.GET.get('dept')
    a=Dept_action_points.objects.filter(department_id__exact=department)
    return render(request, 'dipp/action_ajax.html', {'a': a})


def view_past_target(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        now = timezone.now()
        j=[]
        t=Target.objects.all().filter(end_date__lte= now).order_by('end_date')
        k=[]
        for i in range(0,len(t)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(t,j,k)
        return render(request,'dipp/view_prev_target.html',{'z':z})

def view_current_target(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        now = timezone.now()
        j=[]
        t=Target.objects.all().filter(end_date__gte= now).order_by('end_date')
        print(t)
        k=[]
        for i in range(0,len(t)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(t,j,k)
        return render(request,'dipp/view_current_target.html',{'z':z})


def update_action_points(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        action_no=request.POST.get('action_no')
        action_objective=request.POST.get('action_objective')
        action_description=request.POST.get('action_description')
        now=timezone.now()
        a=ActionPoints.objects.get(action_no=action_no)
        a.action_objective=action_objective
        a.action_description=action_description
        a.update_time=now
        a.save()
        return HttpResponseRedirect(reverse('dipp_home'))

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('login'))

def view_target_analysis(request):

    dept=DeptOfficer.objects.all()
    c=[]
    t_a=[]
    t_na=[]
    for i in dept:
        category={"label":i.dept_name}
        t_achieved=Target.objects.filter(department_id=i.dept_loginid,status='1')
        t_nachieved=Target.objects.filter(department_id=i.dept_loginid,status='0')
        Delay=Notify.objects.filter(department=i.dept_name,type='Delay')
        d3={"value":(len(t_achieved))}
        d4={"value":(len(t_nachieved))}
        print(d4)
        t_a.append(d3)
        t_na.append(d4)
        c.append(category)

#jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
    p={
            "chart": {
            "caption": "Target (Completed vs pending)",
            "xAxisName": "department",
            "yAxisName" : "total number",
            "formatnumberscale": "1",
            "drawCrossLine":"1",
            "plotToolText" : "<b>$dataValue</b> apps on $seriesName in $label",
            "theme": "fusion"
            },


            "categories": [{
            "category": c
            }],
            "dataset": [ {
            "seriesname": "Target Achieved",
            "data":  t_a
            }, {
            "seriesname": "Target Not Achieved",
            "data":  t_na
            }]
            }


    p1=json.dumps(p)


    mscol2D = FusionCharts("mscolumn2d", "ex1" , "600", "400", "chart-1", "json",json.dumps(p))
    return render(request, 'dipp/view_target_analysis.html', {'output': mscol2D.render(), 'chartTitle': ''})




def view_achievement_analysis(request):

    dept=DeptOfficer.objects.all()
    c=[]
    d=[]
    a=[]
    for i in dept:
        category={"label":i.dept_name}
        Achievements=Notify.objects.filter(department=i.dept_name,type='Achievement')
        Delay=Notify.objects.filter(department=i.dept_name,type='Delay')
        d3={"value":(len(Achievements))}
        d4={"value":(len(Delay))}
        a.append(d3)
        d.append(d4)
        c.append(category)

#jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
    p={
            "chart": {
            "caption": "Achievement vs delay",
            "xAxisName": "department",
            "yAxisName" : "total number",
            "formatnumberscale": "1",
            "drawCrossLine":"1",
            "plotToolText" : "<b>$dataValue</b> apps on $seriesName in $label",
            "theme": "fusion"
            },


            "categories": [{
            "category": c
            }],
            "dataset": [ {
            "seriesname": "Achievement",
            "data":  a
            }, {
            "seriesname": "Delay",
            "data":  d
            }]
            }


    p1=json.dumps(p)


    mscol2D = FusionCharts("mscolumn2d", "ex1" , "600", "400", "chart-1", "json",json.dumps(p))
    return render(request, 'dipp/view_ap_analysis.html', {'output': mscol2D.render(), 'chartTitle': ''})




def view_feedback_analysis(request):

    r=Ranking.objects.all()

    dataSource = OrderedDict()
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Feedback of dept"
    chartConfig["subCaption"] = "Average feedback given by stakeholders"
    chartConfig["xAxisName"] = "Department"
    chartConfig["yAxisName"] = "Rating"
    chartConfig["numberSuffix"] = "Star"
    chartConfig["theme"] = "fusion"
    chartData = OrderedDict()

    for i in r:
        print(i.dept_loginid_id)
        print(i.score2)
        print('hi')
        chartData[i.dept_loginid_id] = float(i.score2)
    dataSource["chart"] = chartConfig
    dataSource["data"] = []
    print(chartData.items())

    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)
    column2D = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json", dataSource)
    return  render(request, 'dipp/feedback_analysis.html', {'output' : column2D.render(), 'chartTitle': ''})

##################################################################################################################

def view_comparision_analysis(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        dept = []
        t_a=[]
        t_na=[]
        delay=[]
        achievement=[]
        category_target = []
        category_achievement = []
        d=DeptOfficer.objects.all()
        if request.method=='POST':
            department1=request.POST.get('department1')
            department2=request.POST.get('department2')
            d1 = DeptOfficer.objects.get(dept_name=department1)
            d2 = DeptOfficer.objects.get(dept_name=department2)
            dept.append(d1)
            dept.append(d2)
            for i in dept:
                category={"label":i.dept_name}
                t_achieved=Target.objects.filter(department_id=i.dept_loginid,status='1')
                t_nachieved=Target.objects.filter(department_id=i.dept_loginid,status='0')
                Delay=Notify.objects.filter(department=i.dept_name,type='Delay')
                d3={"value":(len(t_achieved))}
                d4={"value":(len(t_nachieved))}
                #print(d4)
                t_a.append(d3)
                t_na.append(d4)
                category_target.append(category)
            
            target={
                    "chart": {
                    "caption": "Target (Completed vs pending)",
                    "xAxisName": "department",
                    "yAxisName" : "total number",
                    "formatnumberscale": "1",
                    "drawCrossLine":"1",
                    "plotToolText" : "<b>$dataValue</b> apps on $seriesName in $label",
                    "theme": "fusion"
                    },


                    "categories": [{
                    "category": category_target
                    }],
                    "dataset": [ {
                    "seriesname": "Target Achieved",
                    "data":  t_a
                    }, {
                    "seriesname": "Target Not Achieved",
                    "data":  t_na
                    }]
                    }



            mscol2D_target = FusionCharts("mscolumn2d", "ex1" , "600", "400", "target", "json",json.dumps(target))

            for i in dept:
                category={"label":i.dept_name}
                Achievements=Notify.objects.filter(department=i.dept_name,type='Achievement')
                Delay=Notify.objects.filter(department=i.dept_name,type='Delay')
                d3={"value":(len(Achievements))}
                d4={"value":(len(Delay))}
                achievement.append(d3)
                delay.append(d4)
                category_achievement.append(category)

    #jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
            achievement={
                    "chart": {
                    "caption": "Achievement vs delay",
                    "xAxisName": "department",
                    "yAxisName" : "total number",
                    "formatnumberscale": "1",
                    "drawCrossLine":"1",
                    "plotToolText" : "<b>$dataValue</b> apps on $seriesName in $label",
                    "theme": "fusion"
                    },


                    "categories": [{
                    "category": category_achievement
                    }],
                    "dataset": [ {
                    "seriesname": "Achievement",
                    "data":  achievement
                    }, {
                    "seriesname": "Delay",
                    "data":  delay
                    }]
                    }


            mscol2D_achievement = FusionCharts("mscolumn2d", "ex2" , "600", "400", "achievement", "json",json.dumps(achievement))
            return render(request, 'dipp/view_comparision_analysis.html', {'output_target': mscol2D_target.render(), 'output_achievement': mscol2D_achievement.render(), 'chartTitle': '', 'dept':d})
        
        return render(request, 'dipp/view_comparision_analysis.html', {'dept':d})

def sort_by_pm(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        from_date=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        ach=Monitoring_Meeting.objects.all().filter(meeting_date__gte=from_date,meeting_date__lte=to_date)
        n='not uploaded'
        now = timezone.now()
        m=Monitoring_Meeting.objects.all().filter(meeting_date__lte= now).order_by('-meeting_date')
        j=[]
        k=[]
        for i in range(0,len(ach)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(ach,j,k)

        return render(request,'dipp/prev_meetings.html',{'m':z})

def sort_by_date_pnm(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        n='not uploaded'
        now = timezone.now()
        from_date=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        ach=Meeting.objects.all().filter(meeting_date__gte=from_date,meeting_date__lte=to_date)
        j=[]
        k=[]
        for i in range(0,len(ach)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(ach,j,k)

        return render(request,'dipp/prev_normalmeetings.html',{'m':z})

def sort_by_date_um(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        from_date=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        ach=Monitoring_Meeting.objects.all().filter(meeting_date__gte=from_date,meeting_date__lte=to_date)
        now = timezone.now()
        j=[]
        k=[]
        for i in range(0,len(ach)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(ach,j,k)

        return render(request,'dipp/upcoming_meetings.html',{'m':z})

def sort_by_date_unm(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        from_date=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        ach=Meeting.objects.all().filter(meeting_date__gte=from_date,meeting_date__lte=to_date)
        print(ach)
        now = timezone.now()
        j=[]
        k=[]
        for i in range(0,len(ach)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(ach,j,k)

        return render(request,'dipp/upcoming_normalmeetings.html',{'m':z})

def sort_by_date_vct(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        from_date=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        ach=Target.objects.all().filter(end_date__gte=from_date,end_date__lte=to_date)
        now = timezone.now()
        j=[]
        k=[]
        for i in range(0,len(ach)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(ach,j,k)

        return render(request,'dipp/view_current_target.html',{'z':z})

def sort_by_date_vpt(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        from_date=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        ach=Target.objects.all().filter(end_date__gte=from_date,end_date__lte=to_date)
        now = timezone.now()
        j=[]
        k=[]
        for i in range(0,len(ach)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(ach,j,k)

        return render(request,'dipp/view_prev_target.html',{'z':z})

def sort_by_date_vsr_dipp(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        from_date=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        ach=StatusReport.objects.all().filter(month__gte=from_date,month__lte=to_date)
        return render(request,'dipp/view_status_report.html',{'s':ach})

def show_ranking(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        r=Ranking.objects.all()
        max=Ranking.objects.all().aggregate(Max('score1'))
        max=int(max['score1__max'])
        print(max)
        print(type(max))
        #print(max['score1__max'])
        print(r)
        '''for i in r:
            print(i.score1)'''
        l=[]
        if max!=0:
            for i in r:
                print(i.dept_loginid)
                print('hiii')
                print(i.dept_loginid.dept_loginid)
                d=DeptOfficer.objects.get(dept_loginid=i.dept_loginid.dept_loginid)
                print(d)
                score2=float(i.score2)*10
                score1=(float(i.score1)/max)*50
                total=score1+score2
                l.append([d.dept_name,total])
                l.sort(key=lambda x: x[1],reverse=True)
                print(l)
            return render(request,'dipp/show_ranking.html',{'l':l})
        else:
            for i in r:
                print(i.dept_loginid)
                print('hiii')
                print(i.dept_loginid.dept_loginid)
                d=DeptOfficer.objects.get(dept_loginid=i.dept_loginid.dept_loginid)
                print(d)
                score2=float(i.score2)*10
                score1=0
                total=score1+score2
                l.append([d.dept_name,total])
                l.sort(key=lambda x: x[1],reverse=True)
                print(l)
            return render(request,'dipp/show_ranking.html',{'l':l})


def view_ap_analysis(request):
    apoints=ActionPoints.objects.all()
    ac=[]
    t=[]
    a=[]
    delay=[]
    for i in apoints:
        d={"label":i.action_no}
        targets=Target.objects.filter(actionpoint_no_id=i.action_no)
        Achievements=Notify.objects.filter(actionpoint_no_id=i.action_no,type='Achievement')
        Delay=Notify.objects.filter(actionpoint_no_id=i.action_no,type='Delay')
        d2={"value":(len(targets))}
        d3={"value":(len(Achievements))}
        d4={"value":(len(Delay))}
        ac.append(d)
        t.append(d2)
        a.append(d3)
        delay.append(d4)


    print(delay)
    print(type(delay))


#jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
    p={
            "chart": {
            "caption": "Action point wise Analysis",
            "subCaption": "Target, Achievement and Delay",
            "xAxisName": "action point",
            "yAxisName" : "total no",
            "formatnumberscale": "1",
            "drawCrossLine":"1",
            "plotToolText" : "<b>$dataValue</b> apps on $seriesName in $label",
            "theme": "fusion"
            },


            "categories": [{
            "category": ac
            }],
            "dataset": [{
            "seriesname": "Targets Completed",
            "data":  t
            }, {
            "seriesname": "Achievement",
            "data":  a
            }, {
            "seriesname": "Delay",
            "data":  delay
            }]
            }


    p1=json.dumps(p)
    print(p1)
    print(type(p1))


    mscol2D = FusionCharts("mscolumn2d", "ex1" , "600", "400", "chart-1", "json",json.dumps(p))
    return render(request, 'dipp/view_ap_analysis.html', {'output': mscol2D.render(), 'chartTitle': ''})


def download_ap_dipp(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        ap=ActionPoints.objects.all()
        return render(request,'dipp/download_ap_dipp.html',{'ap':ap})


def dept_summary(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        d=DeptOfficer.objects.all()
        l=[]
        main=[]
        for dept in d:
            count=(Target.objects.filter(department_id=dept.dept_loginid).count())
            count_complete=(Target.objects.filter(department_id=dept.dept_loginid,status='1').count())
            l.append([dept.dept_name,count,count_complete])
        main.append(l)
        main=main[0]
        ach=Notify.objects.filter(type='Achievement')
        delay=Notify.objects.filter(type='Delay')
        d=DeptOfficer.objects.all()
        j=[]
        k=[]
        for i in range(0,len(d)):
        	p='#dept_loginid'+str(i)
        	q='dept_loginid'+str(i)
        	j.append(p)
        	k.append(q)
        d=zip(d,j,k)
        return render(request,'dipp/dept_summary.html',{'d':d,'main':main,'ach':ach,'delay':delay})

def auto_monthly_minute(request):
    '''d=DeptOfficer.objects.all()
    for department in d:
        #now = timezone.now()
        datee = datetime.strptime(a, "%Y-%m-%d")
        t=Target.objects.filter(department_id=department.dept_loginid,end_date.month=datee.month)
        print()'''
    
    today = date.today()
    l=[]#actual date
    dlist=[]#string date

    for i in range(1,12):
        print('yes')
        d = today - relativedelta(months=i)
        #c=date(d.year, d.month, 1)
        c=date(d.year, d.month, 1)
    
        l.append(c)
        
        c=str(c)
        c=c[:7]
        #print(type(c))
        #print(c)
        
        dlist.append(c)
        
    t=zip(dlist,l)
    
    return render(request,'dipp/auto_monthly_minute.html',{'t':t})
    
def view_autogenerated_minute(request,j):

    k=j#k for end range
    k=k[:8]+'28'
    t=Target.objects.filter(end_date__range=[j, k])
    achievement=Notify.objects.filter(when__range=[j, k],type='Achievement')
    delay=Notify.objects.filter(when__range=[j,k],type='Delay')
    dept_list=[]
    d=DeptOfficer.objects.all()
    for department in d:
        t=Target.objects.filter(end_date__range=[j, k],department_id=department)
        achievement=Notify.objects.filter(when__range=[j, k],type='Achievement',department=department.dept_name)
        delay=Notify.objects.filter(when__range=[j,k],type='Delay',department=department.dept_name)
        dept_list.append([t,achievement,delay])
        
    #print(dept_list)
    z=zip(d,dept_list)
    
    
    return render(request,'dipp/view_autogenerated_minute.html',{'z':z,})
    