# backend/main/serializers.py
from rest_framework import serializers
from .models import VideoCall

class VideoCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCall
        fields = ['id', 'sender', 'receiver', 'link', 'is_active', 'created_at']
        read_only_fields = ['id', 'link', 'is_active', 'created_at']
