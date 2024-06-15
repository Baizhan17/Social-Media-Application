from .models import Post,Comment,Trend
from account.serializers import UserSerializer
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id','body','created_by','created_at_format','likes_counter')
   



class CommentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id','text','created_by','created_at_format')
         




   
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