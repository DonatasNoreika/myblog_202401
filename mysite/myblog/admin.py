from django.contrib import admin
from .models import Post, Comment, PostPhoto


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class PhotoInLine(admin.TabularInline):
    model = PostPhoto
    extra = 0

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    inlines = [PhotoInLine, CommentInLine]


# Register your models here.
admin.site.register(Post, PostAdmin)
# admin.site.register(Comment)
