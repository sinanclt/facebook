# Generated by Django 3.2.1 on 2021-07-29 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fb', '0024_auto_20210729_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupp',
            name='birthday',
            field=models.DateField(max_length=60),
        ),
    ]