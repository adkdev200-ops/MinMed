from django.contrib import admin
from users.models import Post, PostImage
# Register your models here.
admin.site.register(PostImage)
admin.site.register(Post)