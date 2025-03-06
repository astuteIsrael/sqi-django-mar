from django.contrib import admin
from django.urls import path
# from . import 

from tasks import views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('all_tasks/', views.all_tasks, name='tasks'),

]