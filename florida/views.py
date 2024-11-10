from django.shortcuts import render

def redirect_florida(request):
    return render(request,"load_pixel.html")