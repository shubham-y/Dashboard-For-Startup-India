from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from dept.models import DeptOfficer,Feedback,Ranking
from dipp.models import Monitoring_Meeting
from dipp.models import StatusReport,ActionPoints,Notify,Target
from django.db.models import Max,Count,Q
from dept.fusioncharts import FusionCharts
from collections import OrderedDict
import simplejson as json
# Create your views here.

def stk_hld_home(request):
    if 'sh_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
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
        for i in range (0,len(ap)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        m=zip(ap,j,k)
        main=zip(main,ap,j,k)
        return render(request,'stk_hld/home.html',{'ap':m,'d':d,'main':main})

def view_monitoring_minutes(request):
	if 'sh_username' not in request.session:
		return HttpResponseRedirect(reverse('login'))
	else:
		now = timezone.now()
		m=Monitoring_Meeting.objects.all().filter(meeting_date__lte= now).order_by('-meeting_date')
		n='not uploaded'
		j=[]
		k=[]
		for i in range(0,len(m)):
			d='#id'+str(i)
			e='id'+str(i)
			j.append(d)
			k.append(d)
		z=zip(m,j,k)
	return render(request,'stk_hld/view_monitoring_minutes.html',{'m':z,'n':n})

def view_upcoming_meetings(request):
	if 'sh_username' not in request.session:
		return HttpResponseRedirect(reverse('login'))
	else:
		now=timezone.now()
		m=Monitoring_Meeting.objects.all().filter(meeting_date__gte=now).order_by('-meeting_date')
	j=[]
	k=[]
	for i in range(0,len(m)):
		d='#id'+str(i)
		e='id'+str(i)
		j.append(d)
		k.append(e)
	z=zip(m,j,k)
	return render(request,'stk_hld/view_upcoming_meetings.html',{'m':z})


def view_statusreport_stk(request):
	if 'sh_username' not in request.session:
		return HttpResponseRedirect(reverse('login'))
	else:
		sr=StatusReport.objects.all().order_by('-date_of_upload')
	return render(request,'stk_hld/view_statusreport.html',{'sr':sr})

def view_dept_achievement(request):
	if 'sh_username' not in request.session:
		return HttpResponseRedirect(reverse('login'))
	else:
		ach=Notify.objects.all().filter(type='Achievement').order_by('-when')
		return render(request,'stk_hld/view_dept_achievement.html',{'ach':ach})


def view_past_target_stk(request):
    if 'sh_username' not in request.session:
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
        return render(request,'stk_hld/view_past_target.html',{'z':z})

def view_current_target_stk(request):
    if 'sh_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        now = timezone.now()
        j=[]
        t=Target.objects.all().filter(end_date__gte= now).order_by('end_date')
        k=[]
        for i in range(0,len(t)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        z=zip(t,j,k)
        return render(request,'stk_hld/view_current_target.html',{'z':z})

def feedback_form(request):
    if 'sh_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        j=[]
        d=DeptOfficer.objects.all().distinct()

        for i in range(0,len(d)):
            j.append(i)
        m=zip(d,j)

        return render(request,'stk_hld/feedback_form.html',{'m':m})


def feedback_form_action(request):
    if 'sh_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        d=DeptOfficer.objects.all().distinct()
        f=Feedback.objects.all()
        sh_name=request.session['sh_username']
        t=0
        flag=1
        for i in d:
            print('dept'+str(t))
            rating=request.POST.get('dept'+str(t))
            f=Feedback.objects.all()
            flag=1
            for j in f:
                d1=j.date
                #print(d1)
                d1=str(d1)
                d1=d1[0:7]
                now=timezone.now()
                now=str(now)
                now=now[0:7]
                print(d1)
                print(now)
                print(j.dept)
                print(i.dept_name)
                if d1== now and j.dept==i.dept_name and j.stakeholder==sh_name:#update existing
                    d=DeptOfficer.objects.get(dept_name=i.dept_name)
                    r=Ranking.objects.get(dept_loginid=d.dept_loginid)
                    if r.score2=='0':
                        r.score2=rating
                        r.save()
                    else:
                        temp=(float(r.score2)+int(rating)-int(j.rating))
                        r.score2=str(temp)
                        r.save()
                    j.rating=rating
                    j.save()
                    print('hii')
                    flag=0
                    break
                '''elif j.dept==i.dept_name and j.stakeholder==sh_name and flag!=1:
                    s=Feedback(stakeholder=sh_name,dept=i.dept_name,rating=rating)
                    s.save()
                    print('bye')
                    return HttpResponseRedirect(reverse('stk_hld_home'))'''
            if flag==1:
                d=DeptOfficer.objects.get(dept_name=i.dept_name)
                r=Ranking.objects.get(dept_loginid=d.dept_loginid)
                if r.score2=='0':
                    r.score2=rating
                    r.save()
                else:
                    temp=(float(r.score2)+float(rating))/2
                    r.score2=str(temp)
                    r.save()
                s=Feedback(stakeholder=sh_name,dept=i.dept_name,rating=rating,dept_loginid=i)
                s.save()
            t=t+1
        return HttpResponseRedirect(reverse('stk_hld_home'))

def sort_by_date_dept_achievement(request):
    if 'sh_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        from_date=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        ach=Notify.objects.all().filter(when__gte=from_date,when__lte=to_date)
        return render(request,'stk_hld/view_dept_achievement.html',{'ach':ach})

def sort_by_date_vmm(request):
    if 'sh_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        from_date=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        ach=Monitoring_Meeting.objects.all().filter(meeting_date__gte=from_date,meeting_date__lte=to_date)
        return render(request,'stk_hld/view_monitoring_minutes.html',{'m':ach})

def sort_by_date_vum(request):
    if 'sh_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        from_date=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        ach=Monitoring_Meeting.objects.all().filter(meeting_date__gte=from_date,meeting_date__lte=to_date)
        j=[]
        k=[]
        for i in range(0,len(ach)):
            d='#id'+str(i)
            e='id'+str(i)
            j.append(d)
            k.append(e)
        ach=zip(ach,j,k)
        return render(request,'stk_hld/view_upcoming_meetings.html',{'m':ach})

def sort_by_date_vsr(request):
    if 'sh_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        from_date=request.POST.get('from_date')
        to_date=request.POST.get('to_date')
        ach=StatusReport.objects.all().filter(month__gte=from_date,month__lte=to_date)
        return render(request,'stk_hld/view_statusreport.html',{'sr':ach})

def sh_show_ranking(request):
    if 'sh_username' not in request.session:
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
            return render(request,'stk_hld/sh_show_ranking.html',{'l':l})
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
            return render(request,'stk_hld/sh_show_ranking.html',{'l':l})

def view_target_analysis_stk(request):
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
    return render(request, 'stk_hld/feedback_analysis.html', {'output': mscol2D.render(), 'chartTitle': 'Multiseries Column 2D Chart'})





def view_achievement_analysis_stk(request):

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
            return render(request, 'stk_hld/feedback_analysis.html', {'output': mscol2D.render(), 'chartTitle': 'Multiseries Column 2D Chart'})






def view_comparision_analysis_stk(request):
    if 'sh_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        department = 'department_id__dept_name'
        d=Target.objects.values(department).distinct()
        print(d)
        target=Target.objects.none()
        achievement=Notify.objects.none()

        if request.method=='POST':
            department1=request.POST.get('department1')
            department2=request.POST.get('department2')
            print(department1)
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
        return render(request, 'stk_hld/view_comparision_analysis.html', {'target':target,'achievement':achievement,'dept':d})

def view_feedback_analysis_stk(request):
    if 'sh_username' not in request.session:
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
            print(i.dept_loginid_id)
            print(i.score2)
            print('hi')
            chartData[i.dept_loginid_id] = float(i.score2)
        '''chartData["Venezuela"] = 10
        chartData["Saudi"] = 260
        chartData["Canada"] = 180
        chartData["Iran"] = 140
        chartData["Russia"] = 115
        chartData["UAE"] = 100
        chartData["US"] = 30'''
        dataSource["chart"] = chartConfig
        dataSource["data"] = []
        print(chartData.items())

        for key, value in chartData.items():
            data = {}
            data["label"] = key
            data["value"] = value
            dataSource["data"].append(data)
        column2D = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json", dataSource)
        return  render(request, 'stk_hld/feedback_analysis.html', {'output' : column2D.render(), 'chartTitle': 'Simple Chart Using Array'})

def view_ap_analysis_stk(request):
    if 'sh_username' not in request.session:
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
        return render(request, 'stk_hld/view_ap_analysis.html', {'output': mscol2D.render(), 'chartTitle': 'Multiseries Column 2D Chart'})


def download_ap_sh(request):
    if 'dept_username' not in request.session:
        return HttpResponseRedirect(reverse('login'))
    else:
        ap=ActionPoints.objects.all()
        return render(request,'dept/download_ap_sh.html',{'ap':ap})


def view_dept_summary(request):
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
            return render(request,'stk_hld/view_dept_summary.html',{'d':d,'main':main,'ach':ach,'delay':delay})
