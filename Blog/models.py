from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=15,default=" ")
    email=models.EmailField()

class Post(models.Model):
    title=models.CharField(max_length=15)
    author=models.ForeignKey(User ,on_delete=models.CASCADE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment=models.TextField()
    comment_by=models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_time_date=models.DateTimeField(auto_now_add=True) 

class Like(models.Model):
    like_by=models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_time_date=models.DateTimeField(auto_now_add=True)     