from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [

    path('home/', views.HomePage.as_view(), name='home'),
]

