# Generated by Django 4.0.5 on 2022-06-22 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0003_jobposting_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='qualification',
            field=models.CharField(default='', max_length=100),
        ),
    ]
