from rest_framework.serializers import ModelSerializer

from apps.music.models import Album, Artist


class MiniAuthorSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ('fullname',)


class AlbumListSerializer(ModelSerializer):
    author = MiniAuthorSerializer()
    class Meta:
        model = Album
        fields = ('title', 'author', 'cover')
