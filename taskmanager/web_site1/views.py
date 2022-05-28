from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User, AnonymousUser
from datetime import datetime

from django.template import RequestContext
from django.utils import timezone

from .forms import MyCommentForm, SignUpForm, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME, logout
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    if request.method == 'POST':
        form = MyCommentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            #model_instance.save()
            return redirect('/index')
    else:
        form = MyCommentForm()
        return render(request, 'my_template.html', {'form': form})


def main_site(request):
    return render(request, 'main_site.html')


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'index.html', {'form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Вы вошли как {username}.")
                return redirect('/home')
            else:
                messages.error(request, 'Неверный логин или пароль')
        else:
            messages.error(request, 'Неверный логин или пароль')

    form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/home') # /home
                else:
                    messages.error(request, 'Некорретный аккаунт')
                    #return HttpResponse('Disabled account')
            else:
                messages.error(request, 'Неверный логин или пароль')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form}) #login1




def logout_request(request):
    logout(request)
    messages.info(request, "Выход успешно выполнен!")
    return redirect("/")

def home2(request):
    return render(request, 'home2.html')

@login_required

def aerodrom(request):
    return render(request, 'aerodrom.html')

@login_required

def lecture(request):
    return render(request, 'lecture.html')

@login_required

def port(request):
    return render(request, 'port.html')

@login_required

def gallery(request):
    return render(request, 'gallery.html')

@login_required

def hotel(request):
    return render(request, 'hotel.html')

@login_required

def police(request):
    return render(request, 'police.html')

@login_required

def mansion(request):
    return render(request, 'mansion.html')

@login_required

def white(request):
    return render(request, 'white.html')

@login_required

def science(request):
    return render(request, 'science.html')

@login_required

def flat2(request):
    return render(request, 'flat2.html')

@login_required

def penthouse2(request):
    return render(request, 'penthouse2.html')

@login_required

def vacation2(request):
    return render(request, 'vacation2.html')

@login_required

def pool2(request):
    return render(request, 'pool2.html')

@login_required

def basement2(request):
    return render(request, 'basement2.html')