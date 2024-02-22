from django import forms
from .models import Article

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            "column_name", 
            "headline",
            "subheadline",
            "pub_date", 
            "contributor", 
            "image",
            "content",
            "editor", 
            "category",
        )