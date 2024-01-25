from django.db import models
from django.contrib.auth.forms import User
from tinymce.models import HTMLField
from PIL import Image
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name=_("Photo"), default="profile_pics/default.png", upload_to="profile_pics")

    def __str__(self):
        return _("%s profile") % self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=50)
    author = models.ForeignKey(to=User, verbose_name=_("Author"), on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)
    content = HTMLField(verbose_name=_("Content"))

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-date']

    def num_comments(self):
        return self.comments.all().count()


class PostPhoto(models.Model):
    post = models.ForeignKey(to="Post", on_delete=models.SET_NULL, null=True, blank=True, related_name="photos")
    image = models.ImageField(verbose_name=_("Image"), upload_to="post_photos")

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")


class Comment(models.Model):
    post = models.ForeignKey(to="Post", verbose_name=_("Post"), on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(to=User, verbose_name=_("Author"), on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(verbose_name=_("Date"), auto_now_add=True)
    content = models.TextField(verbose_name=_("Content"), max_length=1000)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['-date']
