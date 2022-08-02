from django.contrib import admin
from .models import Categoreis
from .models import Posts
from .models import Student

# Register your models here.
admin.site.register(Categoreis)
admin.site.register(Posts)
admin.site.register(Student)
