from django.db import models
from martor.models import MartorField


class Info(models.Model):
    firm_name = models.CharField(max_length=256)
    description = MartorField()
    social_description = MartorField()
    url = models.URLField()
    phone = models.CharField(max_length=25)
    logo = models.ImageField()    
    active = models.BooleanField()

    def __str__(self):
        return self.firm_name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["active"],
                condition=models.Q(active=True),
                name="only_one_active",
            ),
        ]


class Section(models.Model):
    published = models.BooleanField()
    slug = models.SlugField()
    title = models.CharField(max_length=150)
    link_text = models.CharField(max_length=64)
    body = MartorField()
    image = models.ImageField()
    
    def __str__(self):
        return self.title
