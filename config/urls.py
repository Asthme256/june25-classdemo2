# """URL configuration for the Django project."""
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('greeting.urls')),
# ]
"""URL configuration for the Django project."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('greeting.urls')),
]



