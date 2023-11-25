
from django.contrib import admin
from django.urls import path
from website1 import views as views_website

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_website.redirect, name='website1')
    
]
