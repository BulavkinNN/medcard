from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='registration.index'),
    path('create/', views.create, name="registration.create"),
]