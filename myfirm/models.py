from django.db import models


class Section(models.Model):
    published = models.BooleanField()
    slug = models.SlugField()
    title = models.CharField(max_length=150)
    link_text = models.CharField(max_length=64)
    body = models.CharField(max_length=3000)
    image = models.ImageField()
