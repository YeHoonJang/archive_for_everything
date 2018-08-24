from django.db import models
from django.utils import timezone
from django.conf import settings

class Contents(models.Model):
    title = models.CharField(max_length=100, default='')
    file = models.FileField()
    author = models.CharField(max_length=50, default='anonymous')
    upload_date = models.DateTimeField('upload date', default=timezone.now())
    counts = models.IntegerField(default=0)
    status = models.CharField(default='uploaded', max_length=10)
