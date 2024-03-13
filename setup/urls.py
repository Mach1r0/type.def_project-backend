from django.urls import path, include
from rest_framework import routers
from album import views as album_views
from user import views as user_views
from artist import views as artist_views

router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'artists', artist_views.ArtistViewSet)
router.register(r'albums', album_views.AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
