from rest_framework.generics import ListAPIView

from apps.music.api_endpoints.Artist.ArtistList.serializers import ArtistListSerializer
from apps.music.models import Artist


class ArtistListView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistListSerializer


__all__ = ('ArtistListView',)
