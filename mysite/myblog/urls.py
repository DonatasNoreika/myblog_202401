from django.urls import path, include
from .views import PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post"),
]