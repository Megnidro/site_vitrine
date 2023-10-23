from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=266)
    email = models.EmailField()
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    email = models.EmailField()
    poste = models.CharField(max_length=255)
    portfolio_cv = models.FileField(upload_to='portfolios/')

    def __str__(self):
        return f"{self.prenoms} {self.nom}"


class TemoignagesModel(models.Model):
    name = models.CharField(max_length=155)
    title_temoignages = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name