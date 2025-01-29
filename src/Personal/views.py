#Personl/views.py
from django.shortcuts import render, HttpResponse, redirect

'''
FUNCTIONS: general 
'''

#FUNCTON: go to home screen
def home_screen_view(request):
    #define some context for what appears on your the homepage
    context = {}

    return render(request, "Personal/home.html", context)

#FUNCTON: go to ogre screen
def go_to_orgre_screen(request):
    print(request.headers)
    return render(request, "Personal/SecretOgre.html", {})
