from django.db import models


# Create your models here.
class ArticleModel(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=100)
    followers = models.ManyToManyField('blog.User', related_name='following')


class Post(models.Model):
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
