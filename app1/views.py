from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def link1(request):
    return render(request,'app1/about1.html')

def link2(request):
    return HttpResponse(" Hello Welcome to app1 link2")

def link3(request):
    return HttpResponse(" Hello Welcome to app1 link3")
