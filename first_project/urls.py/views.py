from django.shortcuts import render, HttpResponse

# Create your views here.

def menu(request):
    return HttpResponse("Welcome to menu page")

def contact(request):
    return HttpResponse("Welcome to contact")