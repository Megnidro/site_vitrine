# Generated by Django 4.2.6 on 2023-10-10 14:07

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OffreEmploi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_offre', models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name="Numéro de l'offre")),
                ('titre', models.CharField(max_length=255, verbose_name='Intitulé du poste')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('description', ckeditor.fields.RichTextField(verbose_name="Description de l'offre")),
                ('qualifications', ckeditor.fields.RichTextField(help_text='Qualifications requises pour le poste')),
                ('responsabilites', ckeditor.fields.RichTextField(blank=True, help_text='Responsabilités associées au poste', null=True)),
                ('lieu', models.CharField(max_length=255, verbose_name='Lieu de travail')),
                ('type_contrat', models.CharField(choices=[('CDI', 'Contrat à durée indéterminée'), ('CDD', 'Contrat à durée déterminée'), ('STAGE', 'Stage'), ('ALTERNANCE', 'Alternance')], max_length=100, verbose_name='Type de contrat')),
                ('salaire', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Salaire proposé')),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('est_active', models.BooleanField(default=True, verbose_name="L'offre est-elle active ?")),
            ],
            options={
                'verbose_name': "Offre d'emploi",
                'verbose_name_plural': "Offres d'emploi",
                'ordering': ['-date_publication'],
            },
        ),
        migrations.CreateModel(
            name='Soumission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom complet')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse e-mail')),
                ('message', ckeditor.fields.RichTextField(verbose_name='Lettre de motivation ou message')),
                ('cv', models.FileField(upload_to='cvs/', verbose_name='CV (fichier)')),
                ('date_soumission', models.DateTimeField(auto_now_add=True, verbose_name='Date de soumission')),
                ('offre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soumissions', to='carriere.offreemploi', verbose_name="Offre d'emploi associée")),
            ],
            options={
                'verbose_name': 'Soumission à une offre',
                'verbose_name_plural': 'Soumissions aux offres',
                'ordering': ['-date_soumission'],
            },
        ),
    ]
