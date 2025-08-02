# from django.apps import AppConfig


# class GreetingConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'greeting'
"""App configuration for the Greeting app."""

from django.apps import AppConfig


class GreetingConfig(AppConfig):
    """Configuration class for the Greeting app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'greeting'

