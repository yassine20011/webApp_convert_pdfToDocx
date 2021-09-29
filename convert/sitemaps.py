from convert.models import Snippet
from django import http
from django.urls import reverse
from django.contrib import sitemaps
from .models import Snippet

class StaticViewsSitemap(sitemaps.Sitemap):
    priority  = 1.0
    changefreq = "daily"

    def items(self):
        return [
        'home',
    ]
    def location(self, items):
        return reverse(items)

class SnippetSitemap(sitemaps.Sitemap):
    
    priority  = 1.0
    changefreq = "daily"

    def items(self):
        return Snippet.objects.all().order_by('id')
