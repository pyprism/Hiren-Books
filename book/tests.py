from django.urls import resolve
from django.test import TestCase, TransactionTestCase
from django.contrib.auth.models import User
from book.views import *
from book.models import Book
from django.test import Client


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

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('hiren', 'a@b.com', 'bunny')

    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_uses_login_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'login.html')

    def test_authenticated_user_redirected(self):
        self.c.login(username='hiren', password='bunny')
        response = self.c.get('/', follow=True)
        self.assertRedirects(response, '/dashboard/')


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

    def test_view_returns_correct_template(self):
        response = self.c.get('/')
        self.assertTemplateUsed(response, 'login.html')


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

    def test_url_resolve_to_correct_view(self):
        slug = Book.objects.get(pk=1)
        found = resolve('/book/' + slug.slug + '/finished')
        self.assertEqual(found.func, book_finished)


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
        response = self.c.post('/add_online/', data={'name': 'hiren', 'url': 'xyz.com', 'type': 'net'}, follow=True)
        self.assertEqual(response.redirect_chain[0][0], '/add_online/')

        book = Book.objects.count()
        self.assertEqual(book, 1)

    def test_url_resolve_to_correct_view(self):
        found = resolve('/add_online/')
        self.assertEqual(found.func, add_book_url)

    def test_view_returns_correct_template(self):
        response = self.c.get('/add_online/')
        self.assertTemplateUsed(response, 'add_online.html')


class AddBookPDFViewTest(TransactionTestCase):
    """
    Test for add_book_pdf
    """
    reset_sequences = True

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('hiren', 'a@b.com', 'bunny')
        self.c.login(username='hiren', password='bunny')

    def test_view_returns_correct_template(self):
        response = self.c.get('/add_pdf/')
        self.assertTemplateUsed(response, 'add.html')

    def test_url_resolve_to_correct_view(self):
        found = resolve('/add_pdf/')
        self.assertEqual(found.func, add_book_pdf)

    def test_book_creation_works(self):
        response = self.c.post('/add_pdf/', data={'name': 'hiren', 'url': 'xyz.com', 'type': 'pdf'}, follow=True)
        self.assertEqual(response.redirect_chain[0][0], '/add_pdf/')

        book = Book.objects.count()
        self.assertEqual(book, 1)


class AddVideoViewTest(TransactionTestCase):
    """
    Test for add_video
    """
    reset_sequences = True

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('hiren', 'a@b.com', 'bunny')
        self.c.login(username='hiren', password='bunny')

    def test_view_returns_correct_template(self):
        response = self.c.get('/add_video/')
        self.assertTemplateUsed(response, 'add_video.html')

    def test_url_resolve_to_correct_view(self):
        found = resolve('/add_video/')
        self.assertEqual(found.func, add_video)

    def test_video_creation_works(self):
        response = self.c.post('/add_video/', data={'name': 'hiren', 'url': 'xyz.com', 'type': 'vid'}, follow=True)
        self.assertEqual(response.redirect_chain[0][0], '/add_video/')

        book = Book.objects.count()
        self.assertEqual(book, 1)


class BookViewTest(TransactionTestCase):
    """
    test for book view
    """
    reset_sequences = True

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user('hiren', 'a@b.com', 'bunny')
        self.c.login(username='hiren', password='bunny')
        Book.objects.create(name="hiren")

    def test_view_returns_correct_template(self):
        slug = Book.objects.get(id=1)
        response = self.c.get('/book/' + slug.slug + '/')
        self.assertTemplateUsed(response, 'book.html')

    def test_url_resolve_to_correct_view(self):
        slug = Book.objects.get(id=1)
        found = resolve('/book/' + slug.slug + '/')
        self.assertEqual(found.func, book)

    def test_information_update_works(self):
        slug = Book.objects.get(id=1)
        response = self.c.post('/book/' + slug.slug + '/', data={'name': 'hiren',
                                                                 'url': 'xyz.com', 'type': 'vid',
                                                                 'note': 'hello hiren :D', 'page_no': 9,
                                                                 'folder': None})
        self.assertRedirects(response, '/book/' + slug.slug + '/')
