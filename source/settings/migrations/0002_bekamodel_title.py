# Generated by Django 4.2.6 on 2023-10-19 07:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bekamodel',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, help_text='Notre histoire', max_length=155),
            preserve_default=False,
        ),
    ]
