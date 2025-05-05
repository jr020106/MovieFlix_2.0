from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    release_date = models.DateField()


class Movie(models.Model):
    title = models.CharField(max_length=200)  # Movie ka title
    image_url = models.URLField()  # Movie ka image URL
    slug = models.SlugField(unique=True)  # Unique slug for URL

    def __str__(self):
        return self.title


