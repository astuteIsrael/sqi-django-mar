from django.urls import path
from . import views

app_name = 'profile_app'

urlpatterns= [
    path('index/', views.index, name= 'index'),
    path('hobbies/', views.hobbies, name= 'hobbies'),
    path('goals/', views.goals, name= 'goals'),
]
