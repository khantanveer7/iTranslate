from django.contrib import admin
from django.urls import path  
from . import views

urlpatterns = [
    path("", views.home, name = 'Home'),
    path("translate", views.translate, name = 'Translate'),
]
