"""hiren URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from book import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r"^logout$", views.logout),
    url(r"^dashboard/$", views.dashboard, name="dashboard"),
    url(r"^add_pdf/$", views.add_book_pdf),
    url(r"^add_online/$", views.add_book_url),
    url(r"^book/(?P<slug>[^\.]+)/finished", views.book_finished),
    url(r"^book/(?P<slug>[^\.]+)/", views.book),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
