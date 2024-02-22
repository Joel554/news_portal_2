from django.urls import path
from .views import editors_list


app_name = "editors"

urlpatterns = [
    path("pop", editors_list, name="editors-list"),
]
