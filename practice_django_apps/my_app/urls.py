from django.urls import path
from my_app import views


urlpatterns = [
    path('my_app/', views.welcome, name="my_App"),
]