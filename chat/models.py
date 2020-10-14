from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    name = models.CharField(max_length=150,null=True,)
    photo = models.ImageField(default='lord.jpg',null=True)
    description = models.TextField(null=True)
    time = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name="blog_post")
    

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
    	return (self.name + "commented")





    