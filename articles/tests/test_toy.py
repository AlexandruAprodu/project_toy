import unittest
from django.contrib.auth.models import AnonymousUser, User
from django.db import transaction
from django.http import Http404
import datetime
from articles.models import Article
from articles.views import articles_edited
from writers.models import Writer
from django.test import RequestFactory, TestCase

from writers.views import dashboard


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

        self.user_writer = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')
        Writer.objects.create(name=self.user_writer, is_editor=False)

        self.user_editor = User.objects.create_user(username='editorr', email='im.an.editor@…', password='top_secret')
        Writer.objects.create(name=self.user_editor, is_editor=True)

    def tearDown(self):
        self.user_writer.writer.delete()
        self.user_editor.writer.delete()
        self.user_writer.delete()
        self.user_editor.delete()

    @transaction.atomic
    def test_writer_cannot_access_edited_articles_page(self):
        request = self.factory.get('/articles-edited')
        request.user = self.user_writer

        with self.assertRaises(Http404):
            articles_edited(request)

    @transaction.atomic
    def test_editor_can_access_edited_articles_page(self):
        request = self.factory.get('articles-edited')
        request.user = self.user_editor
        response = articles_edited(request)

        self.assertEqual(response.status_code, 200)

    @transaction.atomic
    def test_dashboard_shows_correct_data(self):
        article = Article.objects.create(created_at='2021-05-24', title="test title", content="test content",
                               status="PENDING", written_by=self.user_writer.writer, edited_by=None)

        request = self.factory.get('/')
        response = dashboard(request)

        self.assertIn(self.user_writer.username, response.content.decode('utf-8'))
        self.assertNotIn(self.user_editor.username, response.content.decode('utf-8'))

        article.delete()