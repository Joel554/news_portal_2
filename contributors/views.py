from datetime import timezone
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, reverse
from django.views import generic

from main.models import Article
from .models import Contributor
from .forms import ContributorModelForm


def contributor_list(request):
    return render(request, "contributors/contributor_list.html")


class CreateContributorView(generic.CreateView):
    """Editor creates a contributor"""
    template_name = "contributors/contributor_create.html"
    form_class = ContributorModelForm
    
    def get_success_url(self) -> str:
        return reverse("main:editor-ops")


class ListContributorsView(generic.ListView):
    """Editor lists all contributors"""
    model = Contributor
    context_object_name = "contributors"
    template_name = "contributor_list.html"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Contributor.objects.all()
        return queryset
    

class UpdateContributorView(generic.UpdateView):
    """Editor updates a contributor from his account"""
    template = "contributors/contributor_update.html"
    model = Contributor
    form_class = ContributorModelForm

    # def get_queryset(self) -> QuerySet[Any]:
    #     return Contributor.objects.all()
    
    def get_success_url(self) -> str:
        return reverse("main:editor-ops")


class DetailContributorView(generic.DetailView):
    """Editor accesses Editor info"""
    template = "contributors/contributor_detail.html"
    model = Contributor
    context_object_name = "contributor"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        contributor = kwargs['object']
        published_articles = Article.objects.filter(contributor=contributor)
        print(published_articles)
        context.update({
            'published_articles': published_articles,
        })
        return context
    # def get_queryset(self) -> QuerySet[Any]:
    #     return Contributor.objects.all()
    
    # def get_success_url(self) -> str:
    #     return reverse("main:editor-ops")
    




class DeleteContributorView(generic.DeleteView):
    """Editor deletes a contributor from his account"""
    template_name = "contributors/contributor_delete.html"

    def get_queryset(self) -> QuerySet[Any]:
        return Contributor.objects.all()

    def get_success_url(self):
        return reverse("main:editor-ops")


class ListAssignedContributorView():
    pass


class ListContributionsView():
    pass


class RemarkArticleView():
    pass
