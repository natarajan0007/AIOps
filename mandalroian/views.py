from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"chatroom.html")

def netbot(request):
    return render(request,"netbot.html")

def chatwidget(request):
    return render(request,"chatwidget.html")