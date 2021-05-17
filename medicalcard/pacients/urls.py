from django.urls import path
from . import views

app_name = 'pacients'
urlpatterns = [
    path('', views.my_pacients, name='my_pacients'),
]