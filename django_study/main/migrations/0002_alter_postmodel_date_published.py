# Generated by Django 5.0.6 on 2024-05-21 07:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='date_published',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
    ]
