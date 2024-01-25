from django.db import models
from django.contrib.auth.forms import User
from tinymce.models import HTMLField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name="Pavadinimas", max_length=50)
    author = models.ForeignKey(to=User, verbose_name="Autorius", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    content = HTMLField(verbose_name="Tekstas")

    class Meta:
        ordering = ['-date']

    def num_comments(self):
        return self.comments.all().count()


class PostPhoto(models.Model):
    post = models.ForeignKey(to="Post", on_delete=models.SET_NULL, null=True, blank=True, related_name="photos")
    image = models.ImageField(verbose_name="Nuotrauka", upload_to="post_photos")


class Comment(models.Model):
    post = models.ForeignKey(to="Post", verbose_name="Įrašas", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(to=User, verbose_name="Autorius", on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    content = models.TextField(verbose_name="Tekstas", max_length=1000)

    class Meta:
        ordering = ['-date']
