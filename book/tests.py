from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from book.views import *
from book.models import Book
import os


class IndexPageTest(TestCase):

    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)