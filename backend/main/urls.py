# backend/main/urls.py
from django.urls import path
from .views import VideoCallListCreateView, home  # Import the 'home' view

urlpatterns = [
    path('', home, name='home'),  # Root path view
    path('video/', VideoCallListCreateView.as_view(), name='video'),
    # Add more URL patterns as needed
]


