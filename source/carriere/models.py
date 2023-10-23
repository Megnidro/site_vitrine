from django.db import models

# Create your models here.

from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class OffreEmploi(models.Model):
    numero_offre = models.PositiveIntegerField(unique=True, blank=True, null=True, verbose_name="Numéro de l'offre")
    titre = models.CharField(max_length=255, verbose_name="Intitulé du poste")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = RichTextField(verbose_name="Description de l'offre")
    lieu = models.CharField(max_length=255, verbose_name="Lieu de travail")
    type_contrat = models.CharField(max_length=100, choices=[
        ('CDI', 'CDI'),
        ('CDD', 'CDD'),
        ('STAGE', 'Stage'),
        ('ALTERNANCE', 'ALTERNANCE'),
    ], verbose_name="Type de contrat")
    date_publication = models.DateTimeField(auto_now_add=True)
    est_active = models.BooleanField(default=True, verbose_name="L'offre est-elle active ?")



    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        # Gestion du slug
        if not self.slug:
            self.slug = slugify(self.titre)

        # Attribution du numéro de l'offre si non existant
        if not self.numero_offre:
            max_numero = OffreEmploi.objects.all().aggregate(largest=models.Max('numero_offre'))['largest']
            if max_numero:
                self.numero_offre = max_numero + 1
            else:
                self.numero_offre = 1

        super(OffreEmploi, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Offre d'emploi"
        verbose_name_plural = "Offres d'emploi"
        ordering = ['-date_publication']


"""class Soumission(models.Model):
    offre = models.ForeignKey(OffreEmploi, on_delete=models.CASCADE, related_name='soumissions',
                              verbose_name="Offre d'emploi associée")
    nom = models.CharField(max_length=255, verbose_name="Nom complet")
    email = models.EmailField(verbose_name="Adresse e-mail")
    message = RichTextField(verbose_name="Lettre de motivation ou message")
    cv = models.FileField(upload_to='cvs/', verbose_name="CV (fichier)")
    date_soumission = models.DateTimeField(auto_now_add=True, verbose_name="Date de soumission")

    class Meta:
        verbose_name = "Soumission à une offre"
        verbose_name_plural = "Soumissions aux offres"
        ordering = ['-date_soumission']

    def __str__(self):
        return f"{self.nom} - {self.offre.titre}"
"""