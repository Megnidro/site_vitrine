# Generated by Django 4.2.6 on 2023-10-19 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='offre',
            new_name='poste',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='ville_residence',
        ),
    ]
