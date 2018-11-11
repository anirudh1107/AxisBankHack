from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
from . import forms
# Create your views here.

def homeView(request):
    return render(request, 'signatureTest/home.html')

def registerView(request):
    if request.method == "POST":
        form=forms.userForm(request.POST,request.FILES)
        if form.is_valid():
            useritem = form.save(commit=False)
            useritem.save()
    else:
        form=forms.userForm()
    return render(request, 'signatureTest/register.html',{'form':form})

def checkView(request):
    return render(request, 'signatureTest/check.html',{'form':forms.checkForm()})
