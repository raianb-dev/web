from django.shortcuts import render

def redirect(request):
    return render(request,'ca.html')