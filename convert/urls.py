
from django.urls.conf import include
from convert.models import Snippet
from os import name
from django.contrib import sitemaps
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import index, sitemap as sitemap_view
from . import views
from django.contrib.sitemaps.views import sitemap
from convert.sitemaps import SnippetSitemap, StaticViewsSitemap
from django.views.static import serve
from django.views.generic.base import TemplateView 
from django.urls import include, re_path
from django.views.decorators.cache import cache_page
from django.contrib.sitemaps import views as sitemaps_views



sitemaps = {
    'sitemap': StaticViewsSitemap,
    'Snippet': SnippetSitemap
    }

urlpatterns = [
    path('', views.main),
    #path('base/', views.base, name='base'),
    path('home/', views.main, name='home'),
    path('<slug:slug>/', views.Snippet_detail),
    re_path(r'^sitemap.xml$', cache_page(60*60*24)(sitemap_view), {'sitemaps': sitemaps,'content_type':'application/xml'}),
    re_path(r'^robots\.txt', include('robots.urls')),
    #path('media/',views.media, name='media'),
    #url(r'^sitemap1\.xml$', sitemap,{'sitemaps':sitemaps,'content_type':'application/xml'},name='django.contrib.sitemaps.views.sitemap'),
    #path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)