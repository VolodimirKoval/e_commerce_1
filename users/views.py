from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"Вітаємо, {username}! Ви успішно авторизувалися!")
                
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'Авторизація',
        'form': form,
    }
    return render(request, 'users/login.html', context=context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}! Ви вийшли!")
    auth.logout(request)
    return redirect(reverse('main:index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш профіль успішно оновлено!')
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'Профіль',
        'form': form,
    }
    return render(request, 'users/profile.html', context=context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"Вітаємо {user.username}! Ви успішно зареєструвалися!")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Реєстрація',
        'form': form,
    }
    return render(request, 'users/registration.html', context=context)


def user_cart(request):
    context = {
        'title': 'Кошик користувача'
    }
    return render(request, 'users/user-cart.html', context=context)
