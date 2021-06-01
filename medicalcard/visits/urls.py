from django.urls import path
from . import views

app_name = 'visits'
urlpatterns = [
    path('my-visits/', views.my_visits, name='my_visits'),
    path('add/', views.add_visit, name='add_visit'),
    path('visit/<int:pk>', views.get_visit, name='visit'),
    path('visit/edit/<int:pk>', views.edit_visit, name='edit_visit')
]