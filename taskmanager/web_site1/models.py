from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField('Имя', max_length=255, blank=True, null=True)
    surname = models.CharField('Фамилия', max_length=255, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    createAt = models.DateTimeField('Дата', auto_now_add=True)

    def __str__(self):
        return self.name



class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)


from django.db import models


# Create your models here.
class Member(models.Model):
    firstname = models.CharField('Имя', max_length=30)
    lastname = models.CharField('Фамилия', max_length=30)
    username = models.CharField('Логин', max_length=30)
    password = models.CharField('Пароль', max_length=12)

    def __str__(self):
        return self.firstname + " " + self.lastname

    class Meta:
        db_table = "web_member"