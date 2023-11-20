from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from django.views import View
from blog.forms import ArticleForm
from blog.models import ArticleModel


# Create your views here.

class Home(View):
    def get(self, request):
        return HttpResponse('<h1>[GET] Welcome to the Blog Home Page</h1>')

    def post(self, request):
        return HttpResponse('<h1>[POST] Welcome to the Blog Home Page</h1>')


class Article(View):
    def get(self, request):
        return render(request, 'articles.html', {'articles': ArticleModel.objects.all(), 'form': ArticleForm()})

    def post(self, request):
        form = ArticleForm(request.POST)
        form.save()
        return redirect('/blog/articles')


class ArticleDetails(View):
    def get(self, request, id):
        try:
            article = ArticleModel.objects.get(id=id)
            return render(request, 'article_details.html', {'article': article})
        except ArticleModel.DoesNotExist:
            return HttpResponseNotFound('<h1>Article not found</h1>')

    def post(self, request, id):
        article = ArticleModel.objects.get(id=id)
        article.title = request.POST['title']
        article.category = request.POST['category']
        article.author = request.POST['author']
        article.content = request.POST['content']
        article.save()
        return redirect('/blog/articles')
