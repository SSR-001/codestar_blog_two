from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.
class PostList(generic.ListView):
    #reluctant to delete currently
    # queryset = Post.objects.filter(author=4) 
    #reluctant to delete currently
    # queryset = Post.objects.all()
    template_name = "post_list.html"
    queryset = Post.objects.filter(status=1)