from __future__ import unicode_literals
from django.db import models


class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True)
