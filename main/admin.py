from django.contrib import admin
from .models import Teacher, Student, Maintainance, Device
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Maintainance)
admin.site.register(Device)