from rest_framework.serializers import ModelSerializer

from apps.music.models import Song


class SongUpdateSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'cover', 'file', 'genres', 'album')
