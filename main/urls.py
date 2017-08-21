from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    url(r'^search', views.search, name='search'),
    url(r'^results', views.results, name='results'),

]
