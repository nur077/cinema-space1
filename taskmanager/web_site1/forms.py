from django.contrib.auth import authenticate, login
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import Contact
from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm


class MyCommentForm(forms.ModelForm):
    class Meta(object):
        model = Contact
        fields = ['name', 'surname', 'email', 'message']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'surname': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'style':'width:400px;', 'class': 'form-control'}), max_length=30, required=True)
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'style':'width:400px;', 'class': 'form-control'}), max_length=30, required=False)
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'style':'width:400px;', 'class': 'form-control'}), max_length=30, required=False)
    email = forms.EmailField(label='Почта',  widget=forms.PasswordInput(attrs={'style':'width:400px;', 'class': 'form-control'}), max_length=254)
    password1 = forms.CharField(label='Пароль',  widget=forms.PasswordInput(attrs={'style':'width:400px;', 'class': 'form-control'}), max_length=30, required=True)
    password2 = forms.CharField(label='Повторите пароль',  widget=forms.PasswordInput(attrs={'style':'width:400px;', 'class': 'form-control'}), max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

class AuthenticationForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'style':'width:400px;', 'class': 'form-control'}), max_length=40, required=True)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'style':'width:400px;', 'class': 'form-control'}), max_length=40, required=True)

    class Meta:
        model = User
        fields = ('username', 'password')
