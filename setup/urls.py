from django.urls import path, include
from rest_framework import routers
from album import views as album_views
from artist import views as artist_views
from gender import views as genders_views
from users import urls
from django.conf import settings
from django.conf.urls.static import static

# other urls...
router = routers.DefaultRouter()
router.register(r'artists', artist_views.ArtistViewSet)
router.register(r'albums', album_views.AlbumViewSet)
router.register(r'reviews', album_views.ReviewViewSet)
router.register(r'genders', genders_views.GendersViewSet)
router.register(r'subgenrer', genders_views.SubgenresViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)