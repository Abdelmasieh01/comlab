# Generated by Django 4.1.6 on 2023-02-07 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.PositiveSmallIntegerField(choices=[('صالح', 0), ('صيانة', 1), ('تالف', 2)], verbose_name='حالة الجهاز')),
                ('type', models.CharField(max_length=30, verbose_name='نوع الجهاز')),
            ],
        ),
        migrations.CreateModel(
            name='Maintainance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=150, verbose_name='اسم شركة الصيانة')),
                ('start_date', models.DateField(verbose_name='تاريخ البدء')),
                ('duration', models.PositiveSmallIntegerField(verbose_name='مدة أيام الصيانة')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='الاسم')),
                ('day', models.PositiveSmallIntegerField(choices=[('السبت', 0), ('الأحد', 1), ('الاثنين', 2), ('الثلاثاء', 3), ('الاربعاء', 4), ('الخميس', 5)], verbose_name='يوم المدرس بالمعمل')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='الاسم')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher')),
            ],
        ),
    ]
