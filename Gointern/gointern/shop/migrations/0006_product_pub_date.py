# Generated by Django 4.0.5 on 2022-06-24 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_product_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
    ]
