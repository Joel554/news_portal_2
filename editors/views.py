from django.shortcuts import render


# Create your views here.
def editors_list(request):
    return render(request, "editors/editor_list.html")

