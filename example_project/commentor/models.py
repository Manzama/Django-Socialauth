from __future__ import absolute_import
from django.db import models

class Comment(models.Model):
    comment = models.TextField()
