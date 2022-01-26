from django import template
from django.shortcuts import render

# Create your views here.
from django.views.generic import (TemplateView, DetailView, ListView)
from blog.models import Post


class AboutView(TemplateView):
    template_name="blog/about.html"


class PostListView(ListView):
    model =Post

    def get_queryset(self):
        return Post.objects.all.filter(published_date__)