from convert.models import Snippet
from django.urls import reverse
from django.contrib import sitemaps
from .models import Snippet

class StaticViewsSitemap(sitemaps.Sitemap):
    priority  = 1.0
    changefreq = "daily"
    
    def items(self):
        return [
        'pdf-to-docx',
    ]
    def location(self, items):
        return reverse(items)

class SnippetSitemap(sitemaps.Sitemap):
    
    priority  = 1.0
    changefreq = "daily"
    def items(self):
        return Snippet.objects.all().order_by('id')
