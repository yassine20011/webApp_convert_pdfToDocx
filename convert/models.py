from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import FileField
from convert.formatChecker import ContentTypeRestrictedFileField
class img(models.Model):
    File = models.FileField()

class UploadFile(models.Model):
    #content_types=['video/x-msvideo', 'application/pdf', 'video/mp4', 'audio/mpeg', ]
    file = ContentTypeRestrictedFileField(max_upload_size=10485760,content_types=['application/pdf'] , null=True, verbose_name="",default='file', blank= True)
def __str__(self):
        return self.name + ": " + str(self.file)
