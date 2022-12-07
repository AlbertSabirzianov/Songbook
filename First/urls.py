"""First URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from First import settings
from one.views import page, mane_up, add, download, search, run, search_one

urlpatterns = [
    path('admin/', admin.site.urls),
    path('find', page, name='find'), #Новинки!
    path('', mane_up, name='mane'), #Главная страница
    path('add/', add, name='add'), #Добавление песни
    path('run/download/<int:key>', download),
    path('download/<int:key>', download),#Скачивание партий
    path('search', search, name='search'),
    path('search_one', search_one, name="search_one"),#Расширенный поиск
    path('run/', run, name='run')   #Быстрый поиск
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)