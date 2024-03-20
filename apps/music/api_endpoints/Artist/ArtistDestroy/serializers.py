from rest_framework.serializers import ModelSerializer

from apps.music.models import Artist


class ArtistDestroySerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ('avatar', 'fullname')
