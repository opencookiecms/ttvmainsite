# Generated by Django 4.0.3 on 2022-07-20 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_contact_enquirytype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timelinename', models.CharField(blank=True, max_length=50, null=True)),
                ('yearsstring', models.CharField(blank=True, max_length=20, null=True)),
                ('thetitle', models.CharField(blank=True, max_length=150, null=True)),
                ('thedescription', models.TextField(blank=True, null=True)),
            ],
        ),
    ]