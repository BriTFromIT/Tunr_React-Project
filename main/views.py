from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .Serializers import ArtistSerializer, SongSerializer
from .models import Artist, Song


class ArtistView(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer