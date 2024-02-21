from django.db import models
from editors.models import Editor
from contributors.models import Contributor
from categories.models import Category    


class Article(models.Model):
    column_name = models.CharField(max_length=200)
    headline = models.CharField(max_length=200)
    subheadline = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    contributor = models.ForeignKey(
        Contributor, null=True, blank=True, on_delete=models.PROTECT
    )
    image = models.ImageField(null=True, blank=True, upload_to="article_images/")
    content = models.TextField()
    editor = models.ForeignKey(Editor, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.headline
