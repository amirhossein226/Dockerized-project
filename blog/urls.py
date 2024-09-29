from django.urls import path
from . import views
from .feeds import PostFeeds

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<str:post>/',
         views.post_detail, name='post_details'),
    path("tags/<str:tag_slug>/posts/", views.post_list, name="post_by_tag"),
    path("<str:post_slug>/share/", views.post_share, name="post_share"),
    path('<int:post_id>/comments/', views.post_comment, name='post_comment'),
    path('feed/', PostFeeds(), name="post_feeds")
]
