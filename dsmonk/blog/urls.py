from django.urls import path
from . import views

app_name="blog"

urlpatterns = [
    path('', views.AboutView.as_view(), name="blog_about"),

]
