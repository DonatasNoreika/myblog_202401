from django.urls import path, include
from .views import (PostListView,
                    PostDetailView,
                    MyPostListView,
                    MyCommentListView,
                    search,
                    register,
                    profile,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    CommentUpdateView,
                    CommentDeleteView)

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post"),
    path("search/", search, name="search"),
    path("myposts/", MyPostListView.as_view(), name="myposts"),
    path("mycomments/", MyCommentListView.as_view(), name="mycomments"),
    path("register/", register, name="register"),
    path('profile/', profile, name='profile'),
    path("posts/new", PostCreateView.as_view(), name="post_new"),
    path("posts/<int:pk>/update", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name='post_delete'),
    path("post/<int:post_pk>/comments/<int:pk>/update", CommentUpdateView.as_view(), name="comment_update"),
    path("post/<int:post_pk>/comments/<int:pk>/delete", CommentDeleteView.as_view(), name="comment_delete"),
]
