from django.db import models


class Info(models.Model):
    firm_name = models.CharField(max_length=256)
    description = models.CharField(max_length=3000)
    social_description = models.CharField(max_length=3000)
    url = models.URLField()
    phone = models.IntegerField()
    logo = models.ImageField()    


class Section(models.Model):
    published = models.BooleanField()
    slug = models.SlugField()
    title = models.CharField(max_length=150)
    link_text = models.CharField(max_length=64)
    body = models.CharField(max_length=3000)
    image = models.ImageField()
