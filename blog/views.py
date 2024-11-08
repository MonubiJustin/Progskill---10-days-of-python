from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at') # Ordering posts by creation date, newest first
    return render(request, 'blog/post_list.html', {'posts': posts})