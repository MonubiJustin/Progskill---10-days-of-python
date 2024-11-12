from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.create_post, name='create_post'),  # URL to create a new post
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),  # URL to edit a post
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),  # URL for delete functionality
    path('accounts/', include('django.contrib.auth.urls')),
]
