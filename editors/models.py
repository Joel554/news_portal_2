from django.db import models
from categories.models import Category


class Editor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name