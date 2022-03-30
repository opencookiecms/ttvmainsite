# Generated by Django 4.0.3 on 2022-03-30 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_news_ct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventtitle', models.CharField(blank=True, max_length=150, null=True)),
                ('eventcontent', models.TextField(blank=True, null=True)),
                ('eventpic', models.ImageField(blank=True, null=True, upload_to='')),
                ('eventlink', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgtitle', models.CharField(blank=True, max_length=20, null=True)),
                ('imgtitle2', models.CharField(blank=True, max_length=20, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('postlib', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.event')),
            ],
        ),
    ]