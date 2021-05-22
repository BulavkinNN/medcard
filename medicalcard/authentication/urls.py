from django.urls import path
from .views import *


app_name = 'authentication'
urlpatterns = [
    path("login/", LoginCustomView.as_view(), name='login'),
    path("logout/", LogoutCustomView.as_view(), name='logout' ),
    path('password_change/', PasswordChangeCustomView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneCustomView.as_view(), name='password_change_done'),
    path('password_reset/',PasswordResetCustomView.as_view(), name='password_reset'),
    path('password_reset/done/',PasswordResetDoneCustomView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmCustomView.as_view(), name='password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteCustomView.as_view(), name='password_reset_complete')
]


