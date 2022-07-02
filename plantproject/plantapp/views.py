from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(username=username, password=password)
        user.save()

        return redirect('/')
    return render(request,"login.html")
def reg(request):
    return render(request,"reg.html")
def form(request):
    return render(request,"form.html")
def detail(request):
    return render(request,"detail.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
