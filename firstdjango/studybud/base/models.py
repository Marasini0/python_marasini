from msilib.schema import Class
from turtle import heading
from unicodedata import category, name
from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no = models.TextField()
    name = models.TextField(max_length=40)
    stud_class = models.TextField()
    department = models.TextField()
    


class Categoreis(models.Model):
    
    name = models.TextField()
    description = models.TextField(max_length=100)
    status = models.TextField()

class Posts(models.Model):
   
    category_id = models.TextField()
    auth_user_id = models.TextField()
    metatitle = models.TextField()
    metakeyword = models.TextField()
    description = models.TextField(max_length=100)
    heading = models.TextField()
    shortstory = models.TextField(max_length=500)
    fullstory = models.TextField(max_length=5000)
    featureimg = models.TextField()
    created_at = models.TextField()
    updated_at = models.TextField()
    
