from django.shortcuts import render
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', views.index, name="index"),
    
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('logout', views.signin, name="logout"),

    path('settings', views.settings, name="settings"),
    path('profile/<str:pk>', views.profile, name="profile"),

    path('upload', views.upload, name="upload"),
    
    path('like-post', views.like_post, name="like-post"),
    path('follow', views.follow, name="follow"),
    
    path('search', views.search, name="search"),
    
]
