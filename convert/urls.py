
from django.urls.conf import include
from convert.models import Snippet
from os import name
from django.contrib import sitemaps
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap as sitemap_view
from . import views
from django.contrib.sitemaps.views import sitemap
from convert.sitemaps import SnippetSitemap, StaticViewsSitemap
from django.views.static import serve
from django.views.generic.base import TemplateView 
from django.conf.urls import url , include
from django.views.decorators.cache import cache_page



sitemaps = {
    'sitemap': StaticViewsSitemap,
    'Snippet': SnippetSitemap
    }

urlpatterns = [
    path('', views.main),
    #path('base/', views.base, name='base'),
    path('home/', views.main, name='home'),
    path('<slug:slug>/', views.Snippet_detail),
    #path('media/',views.media, name='media'),
    url(r'^robots\.txt', include('robots.urls')),
    url(r'^sitemap.xml$', cache_page(60*60*1)(sitemap), {'sitemaps': sitemaps}, name='cached-sitemap'),
    #path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    #path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)