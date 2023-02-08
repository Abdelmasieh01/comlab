from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('maintainance/', views.maintainance_list, name='maintainance'),
    path('lab/', views.lab_view, name='lab'),
    path('teachers/', views.teachers, name='teachers'),
    path('students/', views.students, name='students'),
]