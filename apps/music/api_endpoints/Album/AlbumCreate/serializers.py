from rest_framework.serializers import ModelSerializer

from apps.music.models import Album


class AlbumCreateSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ('title', 'author', 'cover')
