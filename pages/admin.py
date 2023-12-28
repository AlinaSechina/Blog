from django.contrib import admin

from .models import Post

# отображение модели Post
admin.site.register(Post)
