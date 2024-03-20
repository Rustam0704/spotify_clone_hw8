from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.music.api_endpoints.Album import (
    AlbumListView, AlbumCreateView, AlbumUpdateView, AlbumRetrieveView, AlbumDestroyView)
from apps.music.api_endpoints.Artist import (
    ArtistListView, ArtistDestroyView, ArtistCreateView, ArtistUpdateView, ArtistRetrieveView)
from apps.music.api_endpoints.Song import (
    SongListView, SongCreateView, SongRetrieveView, SongUpdateView, SongDestroyView)

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('songs/', SongListView.as_view()),
    path('song/create/', SongCreateView.as_view()),
    path('song/<pk>/retrieve', SongRetrieveView.as_view()),
    path('song/<pk>/update', SongUpdateView.as_view()),
    path('song/<pk>/destroy', SongDestroyView.as_view()),
    path('artists/', ArtistListView.as_view()),
    path('artist/create/', ArtistCreateView.as_view()),
    path('artist/<pk>/retrieve', ArtistRetrieveView.as_view()),
    path('artist/<pk>/update', ArtistUpdateView.as_view()),
    path('artist/<pk>/destroy', ArtistDestroyView.as_view()),
    path('albums/', AlbumListView.as_view()),
    path('album/create/', AlbumCreateView.as_view()),
    path('album/<pk>/retrieve', AlbumRetrieveView.as_view()),
    path('album/<pk>/update', AlbumUpdateView.as_view()),
    path('album/<pk>/destroy', AlbumDestroyView.as_view()),
]
