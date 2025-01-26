#Test/views.py
from django.shortcuts import render, HttpResponse, redirect
from .forms import CustomUserCreationForm

'''
FUNCTIONS: general 
'''

#FUNCTION: to register
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

'''
FUNCTIONS: navigation
'''
#FUNCTION: to homepage 
def toHomePage(request): 
    return render(request, "home.html")
    #return HttpResponse("Hello World")

# FUNCTION: to account creation page
def toCreateAccountPage(request):
    return render(request, "create_account.html")