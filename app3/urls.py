from django.urls import path
from django.http import HttpResponse
from app3 import views



urlpatterns=[
    
    path('link1/',views.link1),
    path('link2/',views.link2),
    path('link3/',views.link3),

]
