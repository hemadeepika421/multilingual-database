from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from citation import views

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(views.index)
    else:
        form = UserLoginForm()
    return render(request, 'auth/admin_page.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login') 

