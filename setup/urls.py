from django.urls import path, include
from rest_framework import routers
from album import views as album_views
from artist import views as artist_views
from users import urls

router = routers.DefaultRouter()
router.register(r'artists', artist_views.ArtistViewSet)
router.register(r'albums', album_views.AlbumViewSet)
router.register(r'reviews', album_views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('users.urls')),
]