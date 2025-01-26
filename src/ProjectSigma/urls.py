#ProjectSigma/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from Personal.views import home_screen_view
from Personal.views import go_to_orgre_screen


#URLs in our project
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', home_screen_view),
     path('ogre/', go_to_orgre_screen)

    # path("", include("Test.urls")),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
