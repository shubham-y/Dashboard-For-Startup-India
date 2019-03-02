from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from dipp.models import Monitoring_Meeting,Meeting,StatusReport,Notify,Target,ActionPoints,NotificationDipp
from dept.models import DeptOfficer,Ranking,Feedback
from collections import OrderedDict
from django.db.models import Max,Count,Q
from dept.fusioncharts import FusionCharts
from collections import OrderedDict
import simplejson as json
from datetime import date
from dateutil.relativedelta import relativedelta
# Create your views here.

#def dept_home(request):
#    if 'username' not in request.session:
#        return HttpResponseRedirect(reverse('login'))
#    else:
#        return render(request,'dept/home.html')

def dept_home(request):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        userid=request.session['dept_username']
        deptname=DeptOfficer.objects.get(dept_loginid=userid)
        main=[]
        ap=ActionPoints.objects.all()
        for i in range(1,len(ap)+1):
            d=DeptOfficer.objects.all().distinct()
            l=[]
            for dept in d:
                count=(Target.objects.filter(department_id=dept.dept_loginid,actionpoint_no_id=i).count())
                count_complete=(Target.objects.filter(department_id=dept.dept_loginid,actionpoint_no_id=i,status='1').count())
                Achievement=(Notify.objects.filter(department=dept.dept_name,actionpoint_no_id=i,type='Achievement').count())
                Delay=(Notify.objects.filter(department=dept.dept_name,actionpoint_no_id=i,type='Delay').count())
                l.append([dept.dept_name,count,count_complete,Achievement,Delay])
            main.append(l)
        ap=ActionPoints.objects.all()
        j=[]
        k=[]
        d=0
        for i in range (0,len(ap)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        m=zip(ap,j,k)
        main=zip(main,ap,j,k)

        notif = NotificationDipp.objects.all()
        ln = len(notif)
        return render(request,'dept/home.html',{'ap':m,'d':d,'main':main,'dept':dept,'notif':notif,'ln':ln})

def view_upcoming_monitoring_meetings_action_dept(request):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('dept_home'))
    else:
        now = timezone.now()
        m=Monitoring_Meeting.objects.all().filter(meeting_date__gte= now).order_by('meeting_date')
        j=[]
        k=[]
        for i in range(0,len(m)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(m,j,k)
        return render(request,'dept/upcoming_monitoring_meetings.html',{'m':z})

# Got dept_id from session searched it in DeptOfficer db
# Retrieved dept_name for Meeting db and pass thaat row/s
# Test:
    # print(id), print(f.dept_name)
# Pending:
        #Add if else to query of Deptofficer. to show no meetings scheduled

def view_upcoming_individual_meetings_action_dept(request):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('dept_home'))
    else:
        id = request.session['dept_username']
        #print(id)
        now = timezone.now()
        #print(now)
        f=DeptOfficer.objects.all().get(dept_loginid__exact = id)
        f=Meeting.objects.all().filter(meeting_date__gte= now,with_whom__exact = f)
        j=[]
        k=[]
        for i in range(0,len(f)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(f,j,k)
        return render(request,'dept/upcoming_individual_meetings.html',{'m':z})


def view_prev_monitoring_meeting(request):
    if 'dept_username' not in request.session:
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
    return render(request,'dept/prev_meetings.html',{'m':z,'n':n})

# Similar to view_upcoming_individual_meetings_action_dept
# Pending:
    # Displays view minute if entry from db direct in meeting(minute=NULL)
def view_prev_individual_meeting(request):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        now = timezone.now()
        id = request.session['dept_username']
        n='not uploaded'
        f=DeptOfficer.objects.all().get(dept_loginid__exact = id)
        m=Meeting.objects.all().filter(meeting_date__lte= now,with_whom__exact = f)
        return render(request,'dept/prev_individual_meetings.html',{'m':m,'n':n})

def view_status_report_dept(request):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
        now = timezone.now()
    else:
        #s=StatusReport.objects.all().filter(month__gte= now).order_by('meeting_date')
        s=StatusReport.objects.all().order_by('month')
    return render(request,'dept/view_status_report.html',{'s':s})

def notify_dept(request):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        a=ActionPoints.objects.all()
        return render(request,'dept/notify.html',{'a':a})

def notify_action_dept(request):
    n_type=request.POST.get('n_type','NULL')
    desc=request.POST.get('desc','NULL')
    subject=request.POST.get('subject','NULL')
    id = request.session['dept_username']
    actionpoint=request.POST.get('actionpoint','NULL')

    f=DeptOfficer.objects.all().get(dept_loginid__exact = id)
    r=Ranking.objects.all().get(dept_loginid=f.dept_loginid)
    if n_type=='Achievement':
        temp=int(r.score1)+10
        r.score1=str(temp)
        r.save()
    else:
        temp=int(r.score1)-7
        r.score1=str(temp)
        r.save()

    print(f.dept_name)
    department=f.dept_name
    s=Notify(desc=desc,type=n_type,department=department,subject=subject,actionpoint_no_id=actionpoint)
    s.save()
    return HttpResponseRedirect(reverse('notify_dept'))

def view_notification_dept(request):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))

    else:
        #s=StatusReport.objects.all().filter(month__gte= now).order_by('meeting_date')
        n=Notify.objects.all().order_by('-when')
        return render(request,'dept/view_notification.html',{'n':n})


def view_past_target_dept(request):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        id = request.session['dept_username']
        f=DeptOfficer.objects.get(dept_loginid = id)
        now = timezone.now()
        j=[]
        t=Target.objects.all().filter(end_date__lte= now,department=f).order_by('end_date')
        k=[]
        for i in range(0,len(t)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(t,j,k)
        print(f.dept_name)
        return render(request,'dept/view_prev_target_dept.html',{'z':z})

def view_current_target_dept(request):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        id = request.session['dept_username']
        f=DeptOfficer.objects.all().get(dept_loginid__exact = id)
        now = timezone.now()
        j=[]
        t=Target.objects.all().filter(end_date__gte= now,department=f).order_by('end_date')
        k=[]
        for i in range(0,len(t)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(t,j,k)
        return render(request,'dept/view_current_target.html',{'z':z})

def update_status_current_target(request,tid):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    t=Target.objects.all().get(id=tid)
    #print(t.department_id)
    dept=t.department_id
    d=DeptOfficer.objects.get(dept_loginid=dept)
    r=Ranking.objects.get(dept_loginid=d.dept_loginid)
    if t.status == '0':
        temp=int(r.score1)+20
        r.score1=str(temp)
        r.save()
        t.status = '1'
    else:
        temp=int(r.score1)-20
        r.score1=str(temp)
        r.save()
        t.status = '0'
    t.save()
    return HttpResponseRedirect(reverse('view_current_target_dept'))

def update_report_current_target(request,tid):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    report=request.POST.get('report')
    t=Target.objects.all().get(id=tid)
    t.report = report
    t.save()
    return HttpResponseRedirect(reverse('view_current_target_dept'))

def show_ranking_d(request):
    if 'dept_username' not in request.session:
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
            return render(request,'dept/show_ranking_d.html',{'l':l,})
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
            return render(request,'dept/show_ranking_d.html',{'l':l})

def view_target_analysis_dept(request):
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
            #print(d4)
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
        return render(request, 'dept/feedback_analysis.html', {'output': mscol2D.render(), 'chartTitle': ''})



def view_achievement_analysis_dept(request):

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
        return render(request, 'dept/feedback_analysis.html', {'output': mscol2D.render(), 'chartTitle': ''})




def view_comparision_analysis_dept(request):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        department = 'department_id__dept_name'
        d=Target.objects.values(department).distinct()
        #print(d)
        target=Target.objects.none()
        achievement=Notify.objects.none()

        if request.method=='POST':
            department1=request.POST.get('department1')
            department2=request.POST.get('department2')
            #print(department1)
            # department1 = Q()
            # department2 = Q()

            target_1 = Target.objects.filter(department_id__dept_name__exact=department1) \
            .values(department) \
            .annotate(completed_count=Count(department, filter=Q(status=1)), \
                not_completed_count=Count(department, filter=Q(status=0)))
            target_2 = Target.objects.filter(department_id__dept_name__exact=department2) \
            .values(department) \
            .annotate(completed_count=Count(department, filter=Q(status=1)), \
                not_completed_count=Count(department, filter=Q(status=0)))

            achievement_1 = Notify.objects.filter(department__exact=department1) \
            .values('department') \
            .annotate(completed_count=Count('department', filter=Q(type='Achievement')),
                  not_completed_count=Count('department', filter=Q(type='Delay')))
            achievement_2 = Notify.objects.filter(department__exact=department2) \
            .values('department') \
            .annotate(completed_count=Count('department', filter=Q(type='Achievement')),
                  not_completed_count=Count('department', filter=Q(type='Delay')))
            print(target_1)
            print(achievement_2)
            target = target_1.union(target_2)
            achievement = achievement_1.union(achievement_2)

        #print(len(target))
        return render(request, 'dept/view_comparision_analysis.html', {'target':target,'achievement':achievement,'dept':d})

def view_feedback_analysis_dept(request):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:

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
            chartData[i.dept_loginid_id] = float(i.score2)
        dataSource["chart"] = chartConfig
        dataSource["data"] = []
        #print(chartData.items())

        for key, value in chartData.items():
            data = {}
            data["label"] = key
            data["value"] = value
            dataSource["data"].append(data)
        column2D = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json", dataSource)
        return  render(request, 'dept/feedback_analysis.html', {'output' : column2D.render(), 'chartTitle': ''})

def view_ap_analysis_dept(request):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
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
        return render(request, 'dept/view_ap_analysis.html', {'output': mscol2D.render(), 'chartTitle': ''})


def chart(request):

    # Chart data is passed to the `dataSource` parameter, as dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Countries With Most Oil Reserves [2017-18]"
    chartConfig["subCaption"] = "In MMbbl = One Million barrels"
    chartConfig["xAxisName"] = "Country"
    chartConfig["yAxisName"] = "Reserves (MMbbl)"
    chartConfig["numberSuffix"] = "K"
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()
    chartData["Venezuela"] = 10
    chartData["Saudi"] = 260
    chartData["Canada"] = 180
    chartData["Iran"] = 140
    chartData["Russia"] = 115
    chartData["UAE"] = 100
    chartData["US"] = 30



    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)


    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json", dataSource)

    return  render(request, 'dept/chart.html', {'output' : column2D.render(), 'chartTitle': ''})



def download_ap(request):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        ap=ActionPoints.objects.all()
        return render(request,'dept/download_ap.html',{'ap':ap})





def dept_auto_monthly_minute(request):
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
    
    return render(request,'dept/dept_auto_monthly_minute.html',{'t':t})
    
def dept_view_autogenerated_minute(request,j):

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
    
    
    return render(request,'dept/dept_view_autogenerated_minute.html',{'z':z,})
    