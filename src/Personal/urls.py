#Test/urls.py
from django.urls import path 
from . import views


urlpatterns = [
     path("", views.home_screen_view, name = "home"),
      path("ogre/", views.go_to_orgre_screen, name = "ogre"),
    #  path("create-account/", views.toCreateAccountPage, name="create_account"),
    #  path("login/", views.toHomePage, name="login"), 
    #  path('register/', views.register, name='register'),
]