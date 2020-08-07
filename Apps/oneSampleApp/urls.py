from django.contrib import admin
from django.urls import path
from . import views as views_oneSampleApp

urlpatterns = [
    path('', views_oneSampleApp.index, name='index'),
]
