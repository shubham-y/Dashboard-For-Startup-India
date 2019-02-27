from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from dipp.models import DippOfficer
from dept.models import DeptOfficer
from stk_hld.models import StakeHolder
# Create your views here.
def index(request):
    return render(request,'home/index.html')

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
