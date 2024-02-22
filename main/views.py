from django.db.models.query import QuerySet
from django.shortcuts import render, reverse
from django.utils import timezone
from django.views import generic
from .forms import ArticleCreateForm
from typing import Any

from .models import Article
from categories.models import Category
from contributors.models import Contributor


# Article CRUD+L starts : Contributor functionalities
class ArticleListView(generic.ListView):
    """Contributor lists 3 articles for top section"""
    model = Article
    # paginate_by = 1
    context_object_name = "articles"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        cricket_news = Article.objects.filter(category=Category.objects.get(id=3))
        world_news = Article.objects.filter(category=Category.objects.get(id=2))
        india_news = Article.objects.filter(category=Category.objects.get(id=1))
        context.update({
            "cricket_news": cricket_news,
            "world_news": world_news,
            "india_news": india_news,
        })
        return context

    def get_queryset(self):
        user = self.request.user
        queryset = Article.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:3]
        return queryset


class ArticleDetailView(generic.DetailView):
    """Contributor retrieves an article, display all contents"""
    model = Article
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()

        return context


class ArticleUpdateView(generic.UpdateView):
    """Contributor updates Article details"""
    template_name = "main/article_update.html"
    form_class = ArticleCreateForm
    
    def get_queryset(self) -> QuerySet[Any]:
        return Article.objects.all()

    def get_success_url(self) -> str:
        return reverse("main:article-list")


class ArticleCreateView(generic.CreateView):
    """Contributor creates an article"""
    template_name = "main/article_create.html"
    form_class = ArticleCreateForm

    def get_success_url(self) -> str:
        return reverse("main:article-list")


class ArticleDeleteView(generic.DeleteView):
    """Contributor deletes an article"""
    template_name = "main/article_delete.html"

    def get_queryset(self) -> QuerySet[Any]:
        return Article.objects.all()

    def get_success_url(self) -> str:
        return reverse("main:article-list")
    

# Contributor CRUD+L start - Editor responsibilities:
class CreateContributorView():
    """Editor creates a contributor"""
    pass


class UpdateContributorView():
    pass


class DetailContributorView():
    pass


class DeleteContributorView():
    pass


class ListAssignedContributorView():
    pass


class ListContributionsView():
    pass


class RemarkArticleView():
    pass


# Editor CRUD+L : Organizor responsibilities
class CreateEditorView():
    pass


class RetrieveEditorView:
    pass


class UpdateEditorView:
    pass


class DeleteEditorView:
    pass


class ListEditorView:
    pass


# Category CRUD+L : Organizor responsibilities?
class ListCategoryView:
    pass


class CreateCategoryView:
    pass


class RetrieveCategoryView:
    pass


class UpdateCategoryView:
    pass


class DeleteCategoryView:
    pass


class AssignCategoryView:
    # Organizer assigns categories to Editors
    pass


# Article CRUD+L ends
class ContributorOpsView(generic.ListView):
    template_name = "main/contributor_ops.html"
    model = Article
    context_object_name = "articles"

    def get_queryset(self):
        user = self.request.user
        queryset = Article.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )
        return queryset


class AssignEditorView():
    # Organizor assigns editors to contributors
    pass


def editor_ops(request):
    queryset = Contributor.objects.all()
    context ={
        "contributors" :queryset,
    }
    return render(request, "editors/editor_ops.html", context)


# Article CRUD+L ends
class EditorOpsView(generic.ListView):
    template_name = "main/editor_ops.html"
    model = Contributor
    context_object_name = "contributors"

    def get_queryset(self):
        user = self.request.user
        queryset = Contributor.objects.filter()
        return queryset
