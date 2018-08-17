import os
from django.db import models


class Contents(models.Model):
    content_name = models.CharField(max_length=100)
    content_file = models.FileField(upload_to='uploads/')
    content_author = models.CharField(max_length=50)

# class Level(models.Model):
#     content_level = models.
