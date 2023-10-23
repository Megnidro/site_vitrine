from ckeditor.fields import RichTextField
from django.db import models


class BekaModel(models.Model):
    image = models.ImageField(upload_to="bekaimage")
    title = models.CharField(max_length=155, help_text="Notre histoire")
    category = models.CharField(max_length=150)
    description = RichTextField()

    def __str__(self):
        return self.category


class ClientModel(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextField()
    date = models.DateField()
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class EquipeModel(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    image = models.ImageField(upload_to='equipe')

    def __str__(self):
        return self.name


class ProjetModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='equipe')
    description = RichTextField(max_length=100)


