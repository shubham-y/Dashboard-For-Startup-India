from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from dipp.models import DippOfficer
from dept.models import DeptOfficer,Ranking
from stk_hld.models import StakeHolder
from django.db.models import Max
from dept.fusioncharts import FusionCharts
from collections import OrderedDict
import simplejson as json
from datetime import date
from dateutil.relativedelta import relativedelta
from dipp.models import ActionPoints,Target,Notify


# Create your views here.
def index(request):
    #ranking
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
            l=l[0:5]
            print(l)
        #return render(request,'dipp/show_ranking.html',{'l':l})
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
            l=l[0:5]
            print(l)
        #return render(request,'home/index.html',{'l':l})
        #analysis of target
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


    # print(delay)
    # print(type(delay))


#jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
    actionpoint={
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


    # p1=json.dumps(p)
    # print(p1)
    # print(type(p1))


    mscol2D1 = FusionCharts("mscolumn2d", "ex1" , "600", "400", "chart-1", "json",json.dumps(actionpoint))
    return render(request, 'home/index.html', {'output': mscol2D1.render(), 'chartTitle': '','l':l})
    # return render(request, 'dipp/view_comparision_analysis.html', {'dept':d}) 


def login(request):
    return render(request,'home/login.html')

def login_action(request):
    id=request.POST['id']
    password=request.POST['password']

    l= DeptOfficer.objects.filter(dept_loginid=id,dept_password=password)

    if len(l):
        request.session['dept_username']=id #session started
        return HttpResponseRedirect(reverse('dept_home'))

    e=DippOfficer.objects.filter(dipp_loginid=id,dipp_password=password)
    if len(e):
        request.session['username']=id
        return HttpResponseRedirect(reverse('dipp_home'))

    m=StakeHolder.objects.filter(stk_loginid=id,stk_password=password)
    if len(m):
        request.session['sh_username']=id
        return HttpResponseRedirect(reverse('stk_hld_home'))
    else:

        return HttpResponseRedirect(reverse('login')+'?login_failure=true')


def view_stats(request):
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


    # print(delay)
    # print(type(delay))


#jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
    actionpoint={
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


    # p1=json.dumps(p)
    # print(p1)
    # print(type(p1))


    mscol2D1 = FusionCharts("mscolumn2d", "ex1" , "600", "400", "chart-1", "json",json.dumps(actionpoint))

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
    # p1=json.dumps(p)
    mscol2D2 = FusionCharts("mscolumn2d", "ex2" , "600", "400", "chart-2", "json",json.dumps(target))

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


    # p2=json.dumps(p)


    mscol2D3 = FusionCharts("mscolumn2d", "ex3" , "600", "400", "chart-3", "json",json.dumps(achievement))

    return render(request, 'home/view_stats.html', {'output1': mscol2D1.render(), 'output2': mscol2D2.render(),
    'output3': mscol2D3.render(), 'chartTitle': ''})

    return render(request, 'home/view_stats.html', {'output': mscol2D.render(), 'chartTitle': ''})




