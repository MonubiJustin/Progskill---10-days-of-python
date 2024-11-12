from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)                   # Title of the blog post
    content = models.TextField()                               # Content of the post
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Author of the post
    created_at = models.DateTimeField(default=timezone.now)    # Creation date and time
    updated_at = models.DateTimeField(auto_now=True)           # Date and time of the last update

    def __str__(self):
        return self.title
    
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
