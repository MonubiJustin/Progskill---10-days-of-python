from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at') # Ordering posts by creation date, newest first
    return render(request, 'blog/post_list.html', {'posts': posts})

# Retrieve and display the details of a specific post
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})