from django.shortcuts import render
from .models import Teacher, Student, Device, Maintainance


def index(request):
    return render(request, 'main/index.html')


def maintainance_list(request):
    maintainances = Maintainance.objects.all()
    return render(request, 'main/maintainance.html', {'maintainances': maintainances})

def lab_view(request):
    teachers = Teacher.objects.all().count()
    students = Student.objects.all().count()
    devices = Device.objects.all()
    maintainances = Maintainance.objects.all().count()

    return render(request, 'main/lab.html',
                  {
                      'teachers': teachers,
                      'students': students,
                      'devices': devices,
                      'maintainances': maintainances
                  })

def teachers(request):
    teacher_list = Teacher.objects.all()
    return render(request, 'main/teachers.html', {'teachers': teacher_list})

def students(request):
    student_list = Student.objects.all()
    return render(request, 'main/students.html', {'students': student_list})