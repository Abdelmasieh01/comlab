from django.db import models


class Teacher(models.Model):
    satur = 0
    sun = 1
    mon = 2
    tues = 3
    wedns = 4
    thurs = 5
    Choices = [
        (satur, 'السبت'),
        (sun, 'الأحد'),
        (mon, 'الاثنين'),
        (tues, 'الثلاثاء'),
        (wedns, 'الاربعاء'),
        (thurs, 'الخميس')
    ]
    name = models.CharField(max_length=150, verbose_name='الاسم')
    day = models.PositiveSmallIntegerField(
        choices=Choices, verbose_name='يوم المدرس بالمعمل')

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=150, verbose_name='الاسم')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Device(models.Model):
    good = 0
    maintainance = 1
    bad = 2
    Choices = [(good, 'صالح'), (maintainance, 'صيانة'), (bad, 'تالف')]
    state = models.PositiveSmallIntegerField(
        choices=Choices, verbose_name='حالة الجهاز')
    type = models.CharField(max_length=30, verbose_name='نوع الجهاز')

    def __str__(self):
        return self.type


class Maintainance(models.Model):
    company = models.CharField(max_length=150, verbose_name='اسم شركة الصيانة')
    start_date = models.DateField(verbose_name='تاريخ البدء')
    duration = models.PositiveSmallIntegerField(
        verbose_name='مدة أيام الصيانة')

    def __str__(self):
        return 'صيانة من قبل شركة: ' + self.company
