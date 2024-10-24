# Em urls.py
from django.contrib import admin
from django.urls import path
from website1 import views as views_website
from middleware import views as views_notfound
from website2 import views as views_website2
from mines import views as views_mines



urlpatterns = [
    path('', views_website.redirect_get, name='index'),
    path('/app-pregador', views_website.redirect_get, name='app_pregador'),
    path('pt/', views_website.redirect_get, name='index'),
    path('pt/monro/?promo=x7ubsd1/', views_website.redirect_monro, name='promo'),
    path('strada/', views_website2.redirect, name='website2'),
    path('mines/', views_mines.redirect, name='mines'),
    path('homepage/', views_website.bot_page, name='botpage'),

    path('ca/<path:undefined_path>', views_notfound.custom_redirect, name='CA'),
    path('pt/<path:undefined_path>', views_notfound.custom_redirect, name='PT'),
    path('de3vr-e5adp=promo-active?result=yes/', views_website.pixel, name='pixel'),
    path('pixel2/', views_website.pixel2, name='pixel2'),

]

