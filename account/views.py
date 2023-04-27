from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from .forms import UserSignUpForm


# Create your views here.


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html", {"section": "dashboard"})


# Create a new SignUp Form
def sign_up(request):
    if request.method == 'POST':
        sign_up_form = UserSignUpForm(request.POST)
        if sign_up_form.is_valid():
            new_user = sign_up_form.save(commit=False)
            new_user.set_password(sign_up_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/login.html')
    else:
        sign_up_form = UserSignUpForm(request.POST)
    
    return render(request, 'registration/signup.html',{'sign_up_form':sign_up_form})