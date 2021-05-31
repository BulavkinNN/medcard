from django.urls import path
from . import views

app_name = 'visits'
urlpatterns = [
    path('', views.my_visits, name='my_visits'),
]