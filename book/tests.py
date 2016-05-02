from django.core.urlresolvers import resolve
from django.test import TestCase, TransactionTestCase
from django.http import HttpRequest
from django.core.files import File
from django.core.files.storage import Storage
from django.contrib.auth.models import User
from book.views import *
from book.models import Book
import mock


class ModelTest(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        # https://joeray.me/mocking-files-and-file-storage-for-testing-django-models.html
        # file_mock = mock.MagicMock(spec=File, name='FileMock')
        # file_mock.name = 'Hiren.pdf'

        # storage_mock = mock.MagicMock(spec=Storage, name='StorageMock')
        # storage_mock.url = mock.MagicMock(name='url')
        # storage_mock.url.return_value = '/tmp/Hiren.pdf'

        obj = Book()
        obj.note = 'Test note'
        # obj.pdf = file_mock
        # with mock.patch('django.core.files.storage.default_storage._wrapped', storage_mock):
            # The asset is saved to the database but our mock storage
            # system is used so we don't touch the filesystem
        #    obj.save()
        obj.save()

    def test_book_model(self):
        books = Book.objects.all()
        self.assertEqual(books[0].note, 'Test note')
        self.assertEqual(books.count(), 1)


class IndexPageTest(TestCase):

    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_uses_login_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'login.html')