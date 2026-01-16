from django.contrib import admin
from users.models import Post, PostImage


admin.site.register(PostImage)
admin.site.register(Post)