from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('artist', views.ArtistView)
router.register('songs', views.SongView)


urlpatters = [
    path('', include(router.urls))
]