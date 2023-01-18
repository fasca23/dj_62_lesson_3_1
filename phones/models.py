from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.CharField(max_length=100)
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
