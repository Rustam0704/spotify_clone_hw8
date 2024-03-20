from rest_framework.serializers import ModelSerializer

from apps.music.models import Artist


class ArtistRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ('avatar', 'fullname', 'id', 'followers')
