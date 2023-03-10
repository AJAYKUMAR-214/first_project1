from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ajay(request):
    return HttpResponse('<h1><marquee>I am Monster</marquee></h1>')
