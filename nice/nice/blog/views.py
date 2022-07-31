#Import models and form
from audioop import reverse
from multiprocessing import context
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm

#Reverse Classes
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect

# CBV Classes
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import (TemplateView, DetailView, 
                                ListView,CreateView,
                                UpdateView, DeleteView)



class AboutView(TemplateView):
    template_name="blog/about.html"


class PostListView(ListView):
    model =Post
    # context_object_name="post_list"
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model=Post
    

class PostCreateView(LoginRequiredMixin,CreateView):
    login_url=reverse_lazy('social:login')
    redirect_field_name="blog/post_detail.html"
    form_class =PostForm
    model=Post

class PostUdpdateView(LoginRequiredMixin,UpdateView):
    login_url=reverse_lazy('social:login')
    redirect_field_name="blog/post_detail.html"
    form_class =PostForm
    model=Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url=reverse_lazy('social:login')
    success_url=reverse_lazy("blog:blog_post_list")
    model=Post


class DraftListView(LoginRequiredMixin,ListView):
    login_url=reverse_lazy('social:login')
    redirect_field_name="blog/post_list.html"
    model =Post

    
    def get_queryset(self) :
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')





########################################################################
########################################################################

@login_required
def post_publish(request, pk):
    post =get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('blog:blog_post_detail', pk=pk)

@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method =='POST':
        form =CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('blog:blog_post_detail', pk=post.pk)
    else:
        form =CommentForm()

    return render(request,'blog/comment_form.html', context={"form":form})

@login_required
def comment_approve(request, pk):
    comment =get_object_or_404(Comment, pk=pk)
    post_pk=comment.post.pk
    comment.approve()
    return redirect('blog:blog_post_detail', pk=post_pk)

@login_required
def comment_remove(request, pk):
    comment =get_object_or_404(Comment, pk=pk)
    post_pk=comment.post.pk #Save before delete
    comment.delete()
    return redirect('blog:blog_post_detail', pk=post_pk)




    



