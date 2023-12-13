# Em middleware/views.py
from django.shortcuts import render

def redirect(request, path=None):
    return render(request, 'index.html', {'path': path}, status=404)
