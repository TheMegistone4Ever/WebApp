from django.forms import ModelForm
from blog.models import ArticleModel


class ArticleForm(ModelForm):
    class Meta:
        model = ArticleModel
        fields = ['title', 'category', 'author', 'content']
        # OR: exclude = ['creation_date']
