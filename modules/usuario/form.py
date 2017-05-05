# -*- coding: utf-8 -*-
from modules.usuario.models import Usuario

from django import forms

class form_login(forms.Form):

    email = forms.CharField(label="email",max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email','ng-model': 'email'}))
    senha = forms.CharField(label="senha", min_length=8, max_length=20,widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Senha','ng-model': 'senha'}))