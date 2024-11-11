from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Ordering posts by creation date, newest first
    return render(request, 'blog/post_list.html', {'posts': posts})

# Retrieve and display the details of a specific post
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

# View to create a new post
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to the homepage after creating a post
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

# View to edit an existing post
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')  # Redirect to the post list page after deletion
    return render(request, 'blog/delete_post.html', {'post': post})
