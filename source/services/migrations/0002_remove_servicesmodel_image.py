# Generated by Django 4.2.6 on 2023-10-15 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicesmodel',
            name='image',
        ),
    ]
