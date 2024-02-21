from django.contrib import admin
from categories.models import Category
from editors.models import Editor
from contributors.models import Contributor
from main.models import Article


admin.site.register(Category)
admin.site.register(Editor)
admin.site.register(Contributor)
admin.site.register(Article)
