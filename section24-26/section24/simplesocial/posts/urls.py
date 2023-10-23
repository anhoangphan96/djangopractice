from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("", views.PostList.as_view(), name="all"),
    path("new/", views.CreatePost.as_view(), name="create"),
    path("by/<username>/<pk>", views.UserPosts.as_view(), name="detail"),
    path("by/<username>/", views.PostDetail.as_view, name="for_user"),
    path("delete/<pk>/", views.DeletePost.as_view(), name="delete"),
]
