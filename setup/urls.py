from django.urls import path, include
from django.urls import path
from rest_framework import routers
from user import views
from artist import views
from album import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'artist', views.ArtistViewSet)
router.register(r'Album', views.AlbumViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
