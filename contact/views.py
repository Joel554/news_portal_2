from django.shortcuts import render
from django.views import generic


# Create your views here.
def extra_list(request):
    return render(request, "contact/extra.html")

