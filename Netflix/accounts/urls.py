from django.urls import path
from . import views


urlpatterns = [
    path('signup/' , views.SignupPage , name='signup'),
    path('' , views.LoginPage , name='login'),
    path('verify/' , views.OtpPage , name='verify')
]
