from django.test import TestCase
from django.utils.datetime_safe import datetime
from WebApp_Django import settings
from blog.models import ArticleModel
# Create your tests here.
class ArticleTest(TestCase):
    def setUp(self):
        ArticleModel.objects.create(title='test article', category='test category', author='test author', content='test content', creation_date=datetime.now())

    def test_article_created_success(self):
        article = ArticleModel.objects.get(title='test article')
        self.assertEqual(article.author, 'test author')

class BlogPagesTest(TestCase):
    def SetUp(self):
        pass

    def test_home_page_content(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.content, b'<h1>[GET] Welcome to the Blog Home Page</h1>')

