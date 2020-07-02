from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Application1 kinks
def app1_l1(request):
    return HttpResponse(" Hello Welcome to app1 link1")

def app1_l2(request):
    return HttpResponse(" Hello Welcome to app1 link2")

def app1_l3(request):
    return HttpResponse(" Hello Welcome to app1 link3")
#Application2 links
def app2_link1(request):
    return  HttpResponse(" Hello Welcome to app2 link1")

def app2_link2(request):
    return HttpResponse(" Hello Welcome to app2 link2")

def app2_link3(request):
    return  HttpResponse(" Hello Welcome to app2 link3")

#Application3 links
def app3_link1(request):
    return HttpResponse(" Hello Welcome to app3 link1")

def app3_link2(request):
    return HttpResponse(" Hello Welcome to app3 link2")

def app3_link3(request):
    return HttpResponse(" Hello Welcome to app3 link3")
