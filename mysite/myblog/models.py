from django.db import models
from django.contrib.auth.forms import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Pavadinimas", max_length=50)
    author = models.ForeignKey(to=User, verbose_name="Autorius", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    content = models.TextField(verbose_name="Tekstas", max_length=5000)


class Comment(models.Model):
    post = models.ForeignKey(to="Post", verbose_name="Įrašas", on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, verbose_name="Autorius", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    content = models.TextField(verbose_name="Tekstas", max_length=1000)
