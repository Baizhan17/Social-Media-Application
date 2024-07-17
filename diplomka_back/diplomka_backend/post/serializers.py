from .models import Post,Comment,Trend,PostAttachment,PostReport
from account.serializers import UserSerializer
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id','body','created_by','created_at_format','likes_counter','comments_counter')
   



class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id','text','created_by','created_at_format')
         



class PostAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttachment
        fields = ('id', 'image', 'created_by')
   
class PostDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    comments=CommentSerializer(read_only=True,many=True)
    class Meta:
        model = Post
        fields = ('id','body','created_by','created_at_format','likes_counter','comments','comments_counter')
             
             
class TrendSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Trend
        fields = ('id','hashtags','hashtags_counter')
        
        
class PostReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReport
        fields = ('id', 'post', 'text', 'person_reporting', 'created_at')