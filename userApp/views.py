from django.shortcuts import render


from mainAPP import *

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register_user(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register_user')  # Redirect back to registration page
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return redirect('register_user')
        # Create the user
        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        messages.success(request, "You have successfully registered. You can now login.")
        return redirect('login')  # Redirect to login page
    
    return render(request, 'registration/register.html')  # Render registration form template

def log_in_user(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'login.htm')
        
def log_out_user(request):
    logout(request)






