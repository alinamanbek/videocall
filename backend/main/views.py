# backend/main/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import VideoCall
from .serializers import VideoCallSerializer

class VideoCallListCreateView(generics.ListCreateAPIView):
    queryset = VideoCall.objects.all()
    serializer_class = VideoCallSerializer

    def perform_create(self, serializer):
        # Automatically set the sender and generate a unique link
        serializer.save(sender='user123', link=generate_unique_link())

def generate_unique_link():
    # Implement a function to generate a unique link
    # You might use a combination of random characters, timestamp, or other methods
    # Make sure the link is unique in the database
    pass
# backend/main/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Video Chat App!")
