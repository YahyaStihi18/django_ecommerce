# Generated by Django 3.0.6 on 2020-05-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='images/placeholder.png', null=True, upload_to=''),
        ),
    ]
