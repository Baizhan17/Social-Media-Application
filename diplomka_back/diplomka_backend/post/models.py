import uuid
from django.db import models
from account.models import User
from django.utils.timesince import timesince
# Create your models here.


class PostAttachment(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    image=models.ImageField(upload_to="post_attachments")
    created_by=models.ForeignKey(User,related_name="post_attachments",on_delete=models.CASCADE)
class Like(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_by=models.ForeignKey(User,related_name="likes",on_delete=models.CASCADE)
class Comment(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_by=models.ForeignKey(User,related_name="comments",on_delete=models.CASCADE)
    text=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created_at',)
    def created_at_format(self):
        return timesince(self.created_at)
    
    
class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    body=models.TextField(blank=False,null=False)
    attachments=models.ManyToManyField(PostAttachment,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name="posts",on_delete=models.CASCADE)
    likes_counter=models.IntegerField(default=0)
    likes=models.ManyToManyField(Like,blank=True)
    comments=models.ManyToManyField(Comment,blank=True)
    comments_counter=models.IntegerField(default=0)
    class Meta:
        ordering =("-created_at",)
        
    def created_at_format(self):
        return timesince(self.created_at)
    
class Trend(models.Model):
    hashtags = models.CharField(max_length=50)
    hashtags_counter=models.IntegerField()