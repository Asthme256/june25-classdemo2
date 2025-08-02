# """URL routes for greeting app."""

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

"""URL routes for greeting app."""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

