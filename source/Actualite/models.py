from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Actualite(models.Model):
    titre = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    contenu = RichTextField()
    date_publication = models.DateTimeField(default=timezone.now)
    auteur = models.CharField(max_length=100)
    image = models.ImageField(upload_to='actualites/', null=True, blank=True)
    est_publie = models.BooleanField(default=True)
    count = models.PositiveIntegerField(default=0,
                                        help_text="Nombre de fois où l'article a été mis en avant ou partagé.")
    views = models.PositiveIntegerField(default=0, help_text="Nombre de vues de l'article.")

    def increment_views(self):
        self.views += 1
        self.save()

    def increment_count(self):
        self.count += 1
        self.save()

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super(Actualite, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Actualité"
        verbose_name_plural = "Actualités"
        ordering = ['-date_publication']
