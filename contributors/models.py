from django.db import models
from editors.models import Editor


class Contributor(models.Model):
    name = models.CharField(max_length=100)
    editor = models.ForeignKey(
        Editor, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL
        )
    email = models.EmailField()

    def __str__(self):
        return self.name
