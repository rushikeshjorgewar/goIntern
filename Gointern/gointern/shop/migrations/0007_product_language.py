# Generated by Django 4.0.5 on 2022-06-24 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='language',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
