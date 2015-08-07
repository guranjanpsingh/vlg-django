from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/post$', views.detail, name='detail'),
    url(r'^createPost/$', views.createPost, name='createPost'),
    url(r'^likePost/(?P<post_id>[0-9]+)/$', views.likePost, name='likePost'),
    url(r'^dislikePost/(?P<post_id>[0-9]+)/$', views.likePost, name='dislikePost'),
    url(r'^(?P<post_id>[0-9]+)/createComment/$', views.createComment, name='createComment'),
    url(r'^likeComment/(?P<comment_id>[0-9]+)/$', views.likePost, name='likeComment'),
    url(r'^dislikeComment/(?P<comment_id>[0-9]+)/$', views.likePost, name='dislikeComment'),
]
