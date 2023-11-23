from django.test import TestCase
from django.utils.datetime_safe import datetime
from graphene_django.utils import GraphQLTestCase

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


class GraphQLUserTest(GraphQLTestCase):
    fixtures = ['blog/fixtures/users.json']
    def test_retrieve_by_id(self):
        expected = {
            "data": {
                "user": {
                    "id": "2",
                    "name": "Dan Bilzerian",
                    "followers": [
                        {
                            "name": "John Doe"
                        }
                    ]
                },
                "hello": "Hi!"
            }
        }

        response = self.query(
            """
            {
              user(id: 2) {
                id
                name
                followers {
                  name
                }
              }
              hello
            }
            """
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_create_user(self):
        expected = {
            "data": {
                "createUser": {
                    "ok": True,
                    "user": {
                        "id": "3",
                        "name": "Elon Musk"
                    }
                }
            }
        }

        response = self.query(
            """
            mutation createUser {
                createUser(input: {
                    name: "Elon Musk"
                }) {
                    ok
                    user {
                        id
                        name
                    }
                }
            }
            """
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_retrieve_user_with_posts(self):
        expected = {
            "data": {
                "user": {
                    "id": "2",
                    "name": "Dan Bilzerian",
                    "followers": [
                        {
                            "name": "John Doe"
                        }
                    ],
                    "postSet": [
                        {
                            "content": "I love to party!!!"
                        }
                    ]
                }
            }
        }

        response = self.query(
            """
            {
                user(id: 2) {
                    id
                    name
                    followers {
                        name
                    }
                    postSet {
                        content
                    }
                }
            }
            """
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_list_users(self):
        response = self.query(
            """
            {
                users {
                    name
                }
            }
            """
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['data']['users']), 2)
