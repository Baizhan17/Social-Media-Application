from .models import Conversation,ConvMessage
from account.serializers import UserSerializer
from rest_framework import serializers



class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True,many=True)
    class Meta:
        model = Conversation
        fields = ('id','users','modified_at_format')
    



class ConvMessageSerializer(serializers.ModelSerializer):
    receiver = UserSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = ConvMessage
        fields = ('id','text','created_by','created_at_format','receiver')
         



class ConversationDetailSerializer(serializers.ModelSerializer):
    messages = ConvMessageSerializer(read_only=True,many=True)
   # created_by = UserSerializer(read_only=True)
    users = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Conversation
        fields = ('id','users','modified_at_format','messages')
         



