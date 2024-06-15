from django.db import models
from account.models import User
import uuid
from django.utils.timesince import timesince
# Create your models here.
class Conversation(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    users = models.ManyToManyField(User,related_name="conversations")
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    def modified_at_format(self):
        return timesince(self.created_at)
    
class ConvMessage(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    conversation=models.ForeignKey(Conversation,related_name="messages",on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name="messages_delivered",on_delete=models.CASCADE)
    receiver=models.ForeignKey(User,related_name="messages_received",on_delete=models.CASCADE)#sent_to

    def created_at_format(self):
       return timesince(self.created_at)
    