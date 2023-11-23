from django.contrib import admin
from blog.models import ArticleModel
# Register your models here.
@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'creation_date')
