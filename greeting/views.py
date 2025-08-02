# from django.shortcuts import render
# # from django.http import HttpResponse

# def index(request):
#     return render(request, 'index.html', {'greeting': 'Hello'})
"""Views for the Greeting app."""

from django.shortcuts import render


def index(request):
    """Render the index page with a greeting."""
    return render(request, 'index.html', {'greeting': 'Hello'})

