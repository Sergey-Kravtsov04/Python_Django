# Generated by Django 5.0.6 on 2024-05-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_regusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='regusers',
            name='mail',
            field=models.CharField(default='default mail', max_length=200, verbose_name='Mail'),
            preserve_default=False,
        ),
    ]