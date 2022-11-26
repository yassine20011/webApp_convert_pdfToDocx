from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import FileField
from convert.formatChecker import ContentTypeRestrictedFileField
from django.utils.text import slugify
from django.urls import reverse


class img(models.Model):
    File = models.FileField()

class UploadFile(models.Model):
    #content_types=['video/x-msvideo', 'application/pdf', 'video/mp4', 'audio/mpeg', ]
    file = ContentTypeRestrictedFileField(max_upload_size=10485760,content_types=['application/pdf'] , null=True, verbose_name="",default='file', blank= True)

    def __str__(self):
        return str(self.file)


class Snippet(models.Model):

    title = models.CharField(max_length=150)
    slug = models.SlugField(blank=True, null=True)
    body = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return f'/{self.slug}/'