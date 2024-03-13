from django.contrib import admin
from .models import Theme, Post, Comment

# Register your models here.
admin.site.register(Theme)
admin.site.register(Post)
admin.site.register(Comment)
