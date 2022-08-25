# Generated by Django 4.0.3 on 2022-08-16 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_product_productslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.category'),
        ),
    ]