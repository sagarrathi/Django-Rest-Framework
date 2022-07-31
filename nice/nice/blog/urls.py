from django.urls import path
from . import views

app_name="blog"

urlpatterns = [
    path('', views.PostListView.as_view(), name="blog_post_list"),
    path('about', views.AboutView.as_view(), name="blog_about"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="blog_post_detail"),
    path('post/new', views.PostCreateView.as_view(), name="blog_post_create"),
    
    path('drafts', views.DraftListView.as_view(), name="blog_post_draft_list"),
    path('post/<int:pk>/publish/', views.post_publish, name="blog_post_publish"),
    path('post/<int:pk>/edit', views.PostUdpdateView.as_view(), name="blog_post_edit"),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name="blog_post_delete"),
    
    path('post/<int:pk>/comment', views.add_comment_to_post, name="blog_post_comment"),
    path('comment/<int:pk>/approve', views.comment_approve, name="blog_comment_approve"),
    path('comment/<int:pk>/remove', views.comment_remove, name="blog_comment_remove"),
    


    
    
] 
