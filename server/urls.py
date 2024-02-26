# Em urls.py
from django.contrib import admin
from django.urls import path
from website1 import views as views_website
from middleware import views as views_notfound
from website2 import views as views_website2
from mines import views as views_mines



urlpatterns = [
    path('', views_website.redirect, name='index'),
    path('pt/', views_website.redirect, name='website1'),
    path('strada/', views_website2.redirect, name='website2'),
    path('mines/', views_mines.redirect, name='mines'),
    

    path('ca/<path:undefined_path>', views_notfound.custom_redirect, name='CA'),
    path('pt/<path:undefined_path>', views_notfound.custom_redirect, name='PT'),
    path('pixel/', views_website.pixel, name='pixel'),
    path('pixel2/', views_website.pixel2, name='pixel2'),

]

