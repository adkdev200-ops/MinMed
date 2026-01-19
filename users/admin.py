from django.contrib import admin
from users.models import Post, PostImage, Comments, ExtraUserInfo


admin.site.register(PostImage)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(ExtraUserInfo)