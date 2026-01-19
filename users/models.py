from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name ='likes', blank=True)

    def total_likes(self):
        return self.likes.count()

class PostImage(models.Model):
    post = models.ForeignKey(Post,related_name='images', on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/')

class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

class ExtraUserInfo(models.Model):
    user = models.OneToOneField(User,related_name='extrauserinfo', on_delete=models.CASCADE)
    bio = models.TextField(max_length=255, default=None , null=True)
    profile_pic = models.ImageField(upload_to='avatars/', default=None, null=True)