from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.music.api_endpoints.Song.SongRetriewe.serializers import SongRetrieveSerializer
from apps.music.models import Song


class SongRetrieveView(APIView):
    # permission_classes = (IsAuthenticated,)

    @transaction.atomic
    def get(self, request, pk):
        serializer = SongRetrieveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        song_id = serializer.validated_data["songId"]
        song = get_object_or_404(Song, pk=pk)
        song.listened += 1
        song.save()
        return Response(data={"detail": "song listened"})


__all__ = ('SongRetrieveView',)
