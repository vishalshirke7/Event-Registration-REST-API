from django.urls import path

from . import views

app_name = 'userregistration'

urlpatterns = [

    path('register/', views.UserRegistration.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
]