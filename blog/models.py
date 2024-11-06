from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)                   # Title of the blog post
    content = models.TextField()                               # Content of the post
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Author of the post
    created_at = models.DateTimeField(default=timezone.now)    # Creation date and time
    updated_at = models.DateTimeField(auto_now=True)           # Date and time of the last update

    def __str__(self):
        return self.title
