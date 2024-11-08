from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class BlogPostAdmin (admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('author', 'created_at')
