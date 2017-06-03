from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages
from book.models import Book
from book.forms import AddForms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError
import datetime
import logging
# Create your views here.


def index(request):
    """
    Serve index page
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'login.html')


def login(request):
    """
    Handle authentication
    :param request:
    :return:
    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/dashboard/')
        else:
            troll = "Username/Password is not valid! And your password must include " \
                    "a gang sign,a haiku and the blood of a virgin"
            messages.error(request, troll)
            return redirect('/')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


@login_required
def dashboard(request):
    """
    Manage books
    :param request:
    :return:
    """
    books_list = Book.objects.order_by('id')
    paginator = Paginator(books_list, 10)
    page = request.GET.get('page')

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        books = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        books = paginator.page(paginator.num_pages)
    return render(request, 'dashboard.html', {"books": books})


@login_required
def add_book_pdf(request):
    """
    Add book
    :param request:
    :return:
    """
    if request.method == "POST":
        form = AddForms(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, 'New book uploaded and saved')
            except IntegrityError:
                messages.error(request, "The book is already exits")
        else:
            logger = logging.getLogger(__name__)
            messages.error(request, form.errors)
            logger.warning(form.errors)
        return redirect('/add_pdf/')
    else:
        return render(request, 'add.html')


@login_required
def add_book_url(request):
    """
    Add online book
    :param request:
    :return:
    """
    if request.method == "POST":
        form = AddForms(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, 'New Book Added')
            except IntegrityError:
                messages.error(request, "The book is already exits")
        else:
            messages.error(request, "A kitten died in hell !")
        return redirect('/add_online/')
    else:
        return render(request, 'add_online.html')


@login_required
def add_video(request):
    """
    Add video tutorial
    :param request:
    :return:
    """
    if request.method == "POST":
        form = AddForms(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, 'New video added')
            except IntegrityError:
                messages.error(request, "The video is already exits")
        else:
            messages.error(request, "A kitten died in hell !")
        return redirect('/add_video/')
    return render(request, 'add_video.html')


@login_required
def book(request, slug):
    """
    Serve book, take notes etc
    """
    if request.method == 'POST':
        book = Book.objects.get(slug=slug)
        book.note = request.POST.get('note')
        book.page_no = request.POST.get('page_no')
        book.type = request.POST.get('type')
        book.folder = request.POST.get('folder')
        try:
            book.current_url = request.POST.get('current_url')
        except Exception:
            pass
        book.save()
        return redirect(request.path)
    else:
        book = Book.objects.get(slug=slug)
        book_file = '/media/' + str(book.pdf)
        return render(request, 'book.html', {'book_file': book_file, 'book': book, 'url': book.url})


@login_required
def book_finished(request, slug):
    """
    handle book "finish" in model
    :param request:
    :param slug:
    :return:
    """
    book = Book.objects.get(slug=slug)
    book.finished = True
    book.finished_at = datetime.date.today()
    book.save()
    return redirect('/book/' + slug + "/")
