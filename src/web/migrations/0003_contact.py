# Generated by Django 4.0.3 on 2022-06-24 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_news_newspicture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactname', models.CharField(blank=True, max_length=50, null=True)),
                ('companyname', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('contactemail', models.CharField(blank=True, max_length=50, null=True)),
                ('contacttel', models.CharField(blank=True, max_length=20, null=True)),
                ('contactaddress', models.TextField(blank=True, null=True)),
                ('looking', models.CharField(blank=True, max_length=50, null=True)),
                ('enquirysubject', models.CharField(blank=True, max_length=150, null=True)),
                ('enquirycontent', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
