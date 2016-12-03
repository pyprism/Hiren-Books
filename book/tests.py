from django.core.urlresolvers import resolve
from django.test import TestCase, TransactionTestCase
from django.http import HttpRequest
from django.core.files import File
from django.core.files.storage import Storage
from django.contrib.auth.models import User
from book.views import *
from book.models import Book
from django.test import Client
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


class LoginViewTest(TestCase):
    """
    Test for authentication
    """

    def setUp(self):
        User.objects.create_user('hiren', 'a@b.com', 'password')
        self.c = Client()

    def test_login_url_resolves_to_login_view(self):
        found = resolve('/login/')
        self.assertEqual(found.func, login)

    def test_auth_works(self):
        respond = self.c.post('/login/', {'username': 'hiren', 'password': 'password'})
        self.assertRedirects(respond, '/dashboard/')

    def test_redirect_for_unauthenticated_user_works(self):
        response = self.c.get('/dashboard/')
        self.assertRedirects(response, '/?next=/dashboard/')

    def test_redirect_works_for_bad_auth(self):
        respond = self.c.post('/login/', {'username': 'hiren', 'password': 'bad pass'})
        self.assertRedirects(respond, '/')


class LogoutViewTest(TestCase):

    def setUp(self):
        User.objects.create_user('hiren', 'a@b.com', 'password')
        self.c = Client()

    def test_redirect_works(self):
        self.c.post('/login/', {'username': 'hiren', 'password': 'password'})
        respond = self.c.get('/logout')
        self.assertRedirects(respond, '/')


class BookFinishedViewTest(TransactionTestCase):
    """
    Test for book_finished method in view
    """
    reset_sequences = True

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('hiren', 'a@b.com', 'bunny')
        self.c.login(username='hiren', password='bunny')
        Book.objects.create(name="hiren")

    def test_get_method_works(self):
        slug = Book.objects.get(pk=1)
        response = self.c.get('/book/' + slug.slug + '/finished', follow=True)
        self.assertEqual(response.redirect_chain[0][0], '/book/' + slug.slug + '/')

        book = Book.objects.get(pk=1)
        self.assertEqual(book.finished, True)


class OnlineBookAddTest(TransactionTestCase):
    """
    Test add_book_url method works
    """
    reset_sequences = True

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('hiren', 'a@b.com', 'bunny')
        self.c.login(username='hiren', password='bunny')

    def test_online_book_creation_works(self):
        response = self.c.post('/add_online/', data={'name': 'hiren', 'url': 'xyz.com'}, follow=True)
        self.assertEqual(response.redirect_chain[0][0], '/add_online/')

        book = Book.objects.count()
        self.assertEqual(book, 1)
