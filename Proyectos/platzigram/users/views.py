#Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#Exception
from django.db import IntegrityError

#Models
from django.contrib.auth.models import User
from users.models import Profile

def login_view(request):
    """Login a user"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'Error':'Invalid username or password'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('login')


def signup(request):
    """signup view"""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['password']
        passwd_confirmation = request.POST['password_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'Error': 'Password confirmation does not match'})
        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'Error': 'Username is already in user'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')


def update_profile(request):
    """Update a user profile"""
    profile = request.user.profile
    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': request.user.profile,
            'user': request.user,
        }
    )

