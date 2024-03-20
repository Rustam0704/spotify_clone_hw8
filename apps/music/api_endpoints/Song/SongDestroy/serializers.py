from rest_framework.serializers import ModelSerializer

from apps.music.models import Song


class SongDestroySerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ('title', 'cover', 'file', 'genres', 'album')
