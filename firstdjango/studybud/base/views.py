from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from contextlib import contextmanager
from .models import Student
from django.contrib.auth.models import User, auth

# Create your views here
rooms = [
    {'id':1, 'name':'lets learn python'},   #python dictonary
     {'id':2, 'name':'lets learn python2'},
      {'id':3, 'name':'lets learn python3'}
]

# Create your views here.




def home(request):
    context = {'learn':rooms}  #learn is variable and room is view(with value/dictionary)
    #return HttpResponse('Home Page')
    return render(request,'home.html',context)
def about(request):
    context = {'name':'Mina'}
    context = {'office':'Nepal Airlines'}
    #return HttpResponse('About Us')
    return render(request,'about.html',context)
def student_index(request):
    all_students = Student.objects.all()
    num_students = Student.objects.all().count()
    context ={
        'all_students': all_students,
        'num_students': num_students,
    }
    return render(request,'students.html',context)


