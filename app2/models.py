from django.db import models
from django.urls import reverse
from django.contrib import admin

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200, null=False)
    identityNumber = models.CharField(max_length=200, null=False)
    address = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student_edit', kwargs={'pk': self.pk})
        

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # email = models.EmailField()
    

    
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')
 
admin.site.register(User,UserAdmin)