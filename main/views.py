from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Home page')

def about(request):
    return HttpResponse('Home page')