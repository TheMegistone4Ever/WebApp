from django.contrib import admin
from django.urls import path, include
from blog.views import Home, Article, ArticleDetails

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('articles', Article.as_view(), name='article'),
    path('articles/<int:id>', ArticleDetails.as_view(), name='article_details'),
]
