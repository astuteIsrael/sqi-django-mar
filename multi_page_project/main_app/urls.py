from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns= [
    path('home/', views.home, name= 'home'),
    path('contact/', views.contact, name= 'contact'),
    path('about/', views.about, name= 'about'),
]