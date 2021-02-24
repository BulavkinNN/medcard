from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patient', views.index, name='patient'),
    path('doctor', views.index, name='doctor'),

]