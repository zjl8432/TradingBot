from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        #user = username
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def home_view(request):    
    return render(request, 'home.html')

def about_view(request):    
    return render(request, 'about.html')

def contact_view(request):    
    return render(request, 'contact.html')
