from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
# Create your views here.
class PostList(generic.ListView):
    
    template_name = "blog/index.html"
    paginate_by = 6
    queryset = Post.objects.filter(status=1)
    
def post_detail(request, slug):
    """
    display an individual :model:`blog.post`.
    
    **context**
    
    ``post``
        an instance of :model:`blog.post`.
        
        **template:**
        
        :template:`blog/post_detail.html`
    """
    
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    
    return render(
        request,
        "blog/post_detail.html",
        {"post": post,},
    )