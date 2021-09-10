
from os import name
from django.contrib import sitemaps
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.contrib.sitemaps.views import sitemap
from convert.sitemaps import StaticViewsSitemap


sitemaps = {'sitemap': StaticViewsSitemap}

urlpatterns = [
    path('', views.main),
    path('base/', views.base, name='base'),
    path('home/', views.main, name='home'),
    path('media/',views.media, name='media'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
     name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)