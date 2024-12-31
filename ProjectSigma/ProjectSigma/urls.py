#ProjectSigma/urls.py
from django.contrib import admin
from django.urls import path, include


#URLs in our project
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Test.urls")),
]
