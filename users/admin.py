from django.contrib import admin
from users.models import Post, PostImage, Comments


admin.site.register(PostImage)
admin.site.register(Post)
admin.site.register(Comments)
