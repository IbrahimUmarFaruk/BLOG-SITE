from django.test import TestCase

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Article

class ArticleModelTests(TestCase):
    def setUp(self):
        # Create a user to be the author
        self.user = User.objects.create_user(username='testuser', password='password')
        # Create a sample article
        self.article = Article.objects.create(
            title='Test Article', 
            body='This is a test content.',
            author=self.user,
            published=True
        )

    def test_string_representation(self):
        # Test if the article title is returned correctly
        article = Article.objects.get(id=self.article.id)
        self.assertEqual(str(article), 'Test Article')

    def test_article_content(self):
        self.assertEqual(f'{self.article.title}', 'Test Article')
        self.assertEqual(f'{self.article.body}', 'This is a test content.')

class ArticleViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.article = Article.objects.create(
            title='View Test', 
            body='Body content',
            author=self.user,
            published=True
        )

    def test_article_list_view(self):
        # Test if the homepage loads successfully (Status Code 200)
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Test')
        self.assertTemplateUsed(response, 'article_list.html')

    def test_article_detail_view(self):
        # Test if the detail page loads successfully
        response = self.client.get(reverse('article_detail', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Body content')
        self.assertTemplateUsed(response, 'article_detail.html')
