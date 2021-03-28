from django.urls import path

from . import views

app_name = 'medcard'

urlpatterns = [

    path('medcard/patient/', views.patient, name='patient'),
    path('medcard/doctor/', views.doctor, name='doctor'),
    path('medcard/', views.medcard, name='medcard'),
    path('', views.index, name='index'),

]