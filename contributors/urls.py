from django.urls import path
from django.shortcuts import render
from .views import (
    ListContributorsView, 
    CreateContributorView,
    DeleteContributorView,
    UpdateContributorView,
    DetailContributorView,
)


app_name = "contributors"

urlpatterns = [
    path("pop/", ListContributorsView.as_view(), name="list-contributor"),
    path("create/", CreateContributorView.as_view(), name="create-contributor"),
    path("<int:pk>/", DetailContributorView.as_view(), name="contributor-detail"),
    path("<int:pk>/delete/", DeleteContributorView.as_view(), name="delete-contributor"),
    path("<int:pk>/update/", UpdateContributorView.as_view(), name="contributor-update"),

]
