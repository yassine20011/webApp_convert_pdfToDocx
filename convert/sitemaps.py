from django import http
from django.contrib import sitemaps
from django.urls import reverse


class StaticViewsSitemap(sitemaps.Sitemap):

    property = 0.5 
    changefreg = "daily"
    protocol = ['https', 'http']

    def items(self):
        return [
            'main:home',
            'main:media'
            ]

    def location(self, items):
        return reverse(items)