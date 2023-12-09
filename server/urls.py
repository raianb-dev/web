# Em urls.py
from django.contrib import admin
from django.urls import path
from website1 import views as views_website
from middleware import views as views_notfound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_website.redirect, name='website1'),
    path('<path:path>', views_notfound.redirect, name='404')  # Alterado para <path:path>
]
