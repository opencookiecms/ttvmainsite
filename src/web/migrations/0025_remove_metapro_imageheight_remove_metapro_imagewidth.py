# Generated by Django 4.0.3 on 2023-01-11 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_metapro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metapro',
            name='imageheight',
        ),
        migrations.RemoveField(
            model_name='metapro',
            name='imagewidth',
        ),
    ]