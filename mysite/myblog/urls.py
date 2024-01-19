from django.urls import path, include
from .views import PostListView, PostDetailView, search, MyPostListView, MyCommentListView

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post"),
    path("search/", search, name="search"),
    path("myposts/", MyPostListView.as_view(), name="myposts"),
    path("mycomments/", MyCommentListView.as_view(), name="mycomments"),
]
