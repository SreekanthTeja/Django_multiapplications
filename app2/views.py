from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def link1(request):
    return  HttpResponse(" Hello Welcome to app2 link1")

def link2(request):
    return HttpResponse(" Hello Welcome to app2 link2")

def link3(request):
    return  HttpResponse(" Hello Welcome to app2 link3")

