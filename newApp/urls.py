from django.contrib import admin
from django.urls import path, include
from newApp import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.redirect_to_today_post, name='redirect_to_today_post'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('post/<str:date_str>/', views.post, name='post'),
]
