#Test/urls.py
from django.urls import path 
from . import views


urlpatterns = [
     path("", views.toHomePage, name = "home"),
     path("create-account/", views.toCreateAccountPage, name="create_account"),
     path("login/", views.toHomePage, name="login"), 
     path('register/', views.register, name='register'),
]