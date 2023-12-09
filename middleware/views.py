# Em middleware/views.py
from django.shortcuts import render

def redirect(request, path=None):
    return render(request, 'notfound.html', {'path': path}, status=404)
