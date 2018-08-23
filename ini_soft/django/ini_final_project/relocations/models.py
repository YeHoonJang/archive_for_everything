from django.db import models
from django.utils import timezone


class Contents(models.Model):
    title = models.CharField(max_length=100, default='')
    file = models.FileField(upload_to='uploads/')
    author = models.CharField(max_length=50, default='anonymous')
    upload_date = models.DateTimeField('upload date', default=timezone.now())
    counts = models.IntegerField(default=0)
    

class UploadFile(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True)
