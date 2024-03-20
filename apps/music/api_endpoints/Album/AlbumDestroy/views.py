from rest_framework.generics import DestroyAPIView

from apps.music.api_endpoints.Album.AlbumDestroy.serializers import AlbumDestroySerializer
from apps.music.models import Album


class AlbumDestroyView(DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumDestroySerializer


__all__ = ('AlbumDestroyView',)
