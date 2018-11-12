from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^text/$', views.text, name='text'),
    url(r'^json/$', views.json, name='json'),
]
