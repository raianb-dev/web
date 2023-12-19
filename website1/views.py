from django.shortcuts import render

def redirect(request):
    return render(request, 'pt.html')

def pixel(request):
    return render(request, 'pixel.html')

def pixel2(request):
    return render(request, 'pixel2.html')
