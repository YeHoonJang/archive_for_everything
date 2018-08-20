import os
from django.db import models
from django.utils import timezone
import redis


class Contents(models.Model):
    content_name = models.CharField(max_length=100, default='')
    content_file = models.FileField(upload_to='uploads/')
    content_author = models.CharField(max_length=50, default='anonymous')
    upload_date = models.DateTimeField('upload date', default=timezone.now())
    counts = models.IntegerField(default=0)
    
