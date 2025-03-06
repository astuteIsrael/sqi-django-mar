from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("Welcome to home page")

def all_tasks(request):
    return HttpResponse("Welcome to all_tasks")