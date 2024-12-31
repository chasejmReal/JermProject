from django.shortcuts import render, HttpResponse


def helloWorld(request): 
    return render(request, "home.html")
    #return HttpResponse("Hello World")