# backend/main/models.py
from django.db import models
import uuid
from django.utils import timezone

class VideoCall(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    link = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver} - {self.link}"  
class Room(models.Model):
    name = models.TextField()
    label = models.SlugField(unique=True)
    
class Message(models.Model):
    #room = models.ForeignKey(Room, related_name='messages')
    handle = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)