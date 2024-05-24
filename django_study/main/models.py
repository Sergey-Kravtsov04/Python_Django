from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    date_published=models.DateField(default=timezone.now,verbose_name="Дата публикации")
    image = models.ImageField(upload_to="images/", verbose_name="Изображение")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор",null=True,blank=True)
class RegUsers(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    surName = models.CharField(max_length=200, verbose_name="Фамилия")
    age = models.IntegerField( verbose_name="Возраст")
    mail = models.CharField(max_length=200, verbose_name="Mail")
    password = models.CharField(max_length=200,verbose_name="Пароль")

