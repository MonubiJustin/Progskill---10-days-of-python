from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Home page URL
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Detail page for each post
]
