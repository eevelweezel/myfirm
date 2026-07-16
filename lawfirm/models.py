from django.db import models


class Section(models.Model):
    published = models.BooleanField()
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=3000)
