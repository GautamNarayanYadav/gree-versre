from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1 style='font-size:80px; color:red;'>Hello, gautam world. You're at the polls index.")