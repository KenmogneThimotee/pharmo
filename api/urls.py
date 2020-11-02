from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('video/', VideoView.as_view(), name='video'),
    path('comment/', CommentaireView.as_view(), name='comment'),
    path('likeVideo/', LikeVideoView.as_view(), name='likeVideo'),
    path('dislikeVideo/', DislikeVideoView.as_view(), name='dislikeVideo'),
    path('sabonne/', SabonneView.as_view(), name='sabonne'),
    path('desabonne/', DesabonneView.as_view(), name='desabonne'),
    path('playlist/', PlaylistView.as_view(), name='playlist'),
    path('addVideoPlaylist/', AddVideoPlaylistView.as_view(), name='addVideoPlaylist'),
    path('deleteVideoPlaylist/', DeleteVideoPlaylistView.as_view(), name='deleteVideoPlaylist'),
    path('userDetail/', UserView.as_view(), name='userDetail'),
]