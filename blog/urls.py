from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.create_post, name='create_post'),  # URL to create a new post
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),  # URL to edit a post
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),  # URL for delete functionality
]
