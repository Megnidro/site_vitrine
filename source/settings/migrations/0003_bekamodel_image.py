# Generated by Django 4.2.6 on 2023-10-19 07:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_bekamodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='bekamodel',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='bekaimage'),
            preserve_default=False,
        ),
    ]