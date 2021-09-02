
from os import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.main),
    path('base/', views.base, name='base'),
    path('home/', views.main, name='home'),
    path('media/',views.media, name='media'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)