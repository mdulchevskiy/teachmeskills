from django.db import models
from django.utils import timezone


class Shortener(models.Model):
    long_url = models.CharField(max_length=510)
    short_url = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    clicks = models.IntegerField(default=0)
