from django.urls import path
from .views import extra_list


app_name = "contact"

urlpatterns = [
    path("pop", extra_list),
]
