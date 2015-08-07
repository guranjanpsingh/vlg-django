from django.db import models

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=2000)
    postedOn = models.DateTimeField()
    postedBy = models.CharField(max_length=30)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.post

class Comment(models.Model):
    comment = models.CharField(max_length=2000)
    postsID = models.ForeignKey(Post)
    postedBy = models.CharField(max_length=30)
    postedOn = models.DateTimeField()
    def __str__(self):
        return self.comment

class PostLikes(models.Model):
    postsID = models.ForeignKey(Post)
    likedBy = models.CharField(max_length=30)

class PostDisikes(models.Model):
    postsID = models.ForeignKey(Post)
    dislikedBy = models.CharField(max_length=30)

class commentLikes(models.Model):
    commentsID = models.ForeignKey(Comment)
    likedBy = models.CharField(max_length=30)

class commentDislikes(models.Model):
    commentsID = models.ForeignKey(Post)
    dislikedBy = models.CharField(max_length=30)
