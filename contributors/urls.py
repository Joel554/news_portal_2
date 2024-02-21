from django.urls import path
from django.shortcuts import render
from .views import contributor_list


app_name = "contributors"

urlpatterns = [
    path("pop", contributor_list),
]
