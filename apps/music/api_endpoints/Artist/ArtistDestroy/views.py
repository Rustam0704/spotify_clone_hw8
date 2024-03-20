from rest_framework.generics import DestroyAPIView

from apps.music.api_endpoints.Artist.ArtistDestroy.serializers import ArtistDestroySerializer
from apps.music.models import Artist


class ArtistDestroyView(DestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistDestroySerializer


__all__ = ('ArtistDestroyView',)
