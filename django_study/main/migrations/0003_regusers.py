# Generated by Django 5.0.6 on 2024-05-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_postmodel_date_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('surName', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('password', models.CharField(max_length=200, verbose_name='Пароль')),
            ],
        ),
    ]
