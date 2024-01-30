# backend/video/urls.py
from django.contrib import admin
from django.urls import include, path
from main.views import VideoCallListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),  # Include the admin URLs
    path('', include('main.urls')),  # Include main app URLs
    # Add other URL patterns as needed
]
