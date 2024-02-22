from django.urls import path
from .views import (
    ArticleDetailView, 
    ArticleListView,
    ArticleUpdateView,
    ArticleCreateView,
    ArticleDeleteView,
    ContributorOpsView,
    editor_ops,
)

app_name = "main"

urlpatterns = [
    path("", ArticleListView.as_view(), name="article-list"),
    path("create", ArticleCreateView.as_view(), name="article-create"),
    path("contributor_ops", ContributorOpsView.as_view(), name="contributor-ops"),
    path("editor_ops", editor_ops, name="editor-ops"),
    path("<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path("<int:pk>/update", ArticleUpdateView.as_view(), name="article-update"),
    path("<int:pk>/delete", ArticleDeleteView.as_view(), name="article-delete"),
]
