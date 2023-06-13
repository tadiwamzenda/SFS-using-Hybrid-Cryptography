from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django import forms
import requests

def flask_app_view(request):
    # Make a GET request to your Flask app
    response = requests.get('http://127.0.0.1:5000/')
    
    # Extract the response content from the request
    content = response.content.decode('utf-8')
    
    # Render the response content in a template or return it directly
    return render(request, 'flask_app.html', {'content': content})


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

class SignupForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput)

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("Password must contain at least 1 digit.")
        if not any(char.isupper() for char in password1):
            raise forms.ValidationError("Password must contain at least 1 uppercase letter.")
        if not any(char.islower() for char in password1):
            raise forms.ValidationError("Password must contain at least 1 lowercase letter.")
        return password1

def SignupPage(request):
    if request.method=='POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            uname=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            pass1=form.cleaned_data.get('password1')
            pass2=form.cleaned_data.get('password2')

            if pass1!=pass2:
                messages.warning(request, 'Password mismatch!')
                return redirect('signup')

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            
            messages.success(request, 'User created successfully!')
            return redirect('login')
        else:
            # Form data is invalid, redisplay the form with error messages
            context = {
                'form': form
            }
            return render(request, 'signup.html', context)
    else:
        # GET request, display the empty form
        form = SignupForm()

    context = {
        'form': form
    }

    return render(request, 'signup.html', context)

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('http://127.0.0.1:5000/')

        else:

            messages.warning(request, 'Invalid Username or Password!')

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
