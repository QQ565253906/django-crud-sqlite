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