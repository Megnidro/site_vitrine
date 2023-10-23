from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class ServicesModel(models.Model):
    icon_class = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True, default="")
    content = RichTextField()
    category = models.CharField(max_length=155)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    is_home = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    """@property
    def author_or_default(self):
        return self.author.username if self.author else "L'auteur inconnu"
"""

    def get_absolute_url(self):
        return reverse('posts:post', kwargs={'slug': self.slug})


class ProjetModel(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True, default="")
    content = RichTextField()
    category = models.CharField(max_length=155)
    image = models.ImageField()

    def __str__(self):
        return self.title
