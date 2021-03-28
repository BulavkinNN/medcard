from django.urls import path
from .views import LoginCustomView, LogoutCustomView


app_name = 'authentication'
urlpatterns = [
    path("login/", LoginCustomView.as_view(), name='login'),
    path("logout/", LogoutCustomView.as_view(), name='logout' ),

]


