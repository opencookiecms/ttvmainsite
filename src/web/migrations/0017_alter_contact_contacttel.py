# Generated by Django 4.0.3 on 2022-11-30 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_alter_category_catype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contacttel',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
