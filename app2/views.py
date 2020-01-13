from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Student
import csv

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
 
    writer = csv.writer(response)
    writer.writerow(['Name', 'IdentityNumber',])
 
    users = Student.objects.all().values_list('name', 'identityNumber')
    for user in users:
        writer.writerow(user)
 
    return response

def dl(request):
    return render(request,"download.html")
    
# Create your views here.

class StudentList(ListView):
    model = Student

class StudentDetail(DetailView):
    model = Student

class StudentCreate(CreateView):
    model = Student
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('student_list')

class StudentUpdate(UpdateView):
    model = Student
    fields = ['name', 'identityNumber', 'address', 'department']
    success_url = reverse_lazy('student_list')

class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')
    
#coding=utf-8
# from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django import forms
from .models import User
# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
    # email = forms.EmailField(label='邮箱')

def regist(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            # email = userform.cleaned_data['email']
            # User.objects.create(username=username,password=password,email=email)
            user=User.objects.create(username=username,password=password)
            user.save()

            return HttpResponse('regist success!!!')
    else:
        userform = UserForm()
    return render(request,'regist.html',{'userform':userform})

def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']

            user = User.objects.filter(username__exact=username,password__exact=password)

            if user:
                return render(request,'index.html',{'userform':userform})
            else:
                return HttpResponse('用户名或密码错误,请重新登录')

    else:
        userform = UserForm()
    return render(request,'login.html',{'userform':userform})
