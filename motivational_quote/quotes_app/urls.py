from django.urls import path

from . import views

urlpatterns = [
    path("quotes/", views.welcome, name="quotes"),
]