from django.shortcuts import render


# Create your views here.
def contributor_list(request):
    return render(request, "contributors/contributor_list.html")

