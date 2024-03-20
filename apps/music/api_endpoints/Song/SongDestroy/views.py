from rest_framework.generics import DestroyAPIView

from apps.music.api_endpoints.Song.SongDestroy.serializers import SongDestroySerializer
from apps.music.models import Song


class SongDestroyView(DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongDestroySerializer


__all__ = ('SongDestroyView',)
