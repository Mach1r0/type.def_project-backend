from django.urls import path, include
from rest_framework import routers
from album import views as album_views
from artist import views as artist_views
from user.views import UserView  # Import the UserView

router = routers.DefaultRouter()
router.register(r'artists', artist_views.ArtistViewSet)
router.register(r'albums', album_views.AlbumViewSet)
router.register(r'reviews', album_views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserView.as_view({'get': 'list', 'delete': 'destroy', 'put': 'retrieve' }), name='user-list'),
    path('users/<int:pk>/', UserView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name='user-detail'),
    path('users/create/', UserView.as_view({'post': 'create'}), name='user-create'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]