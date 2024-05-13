from django.urls import path, include
from rest_framework import routers
from album import views as album_views
from artist import views as artist_views
from gender import views as genders_views
from users import urls
from django.conf import settings
from django.conf.urls.static import static
from album.views import count_view
from artist.views import count_artist
from music import views as music_view
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin

schema_view = get_schema_view(
   openapi.Info(
      title="",
      default_version='v1',
      description="API description",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'music', music_view.MusicViewSet)
router.register(r'artists', artist_views.ArtistViewSet)
router.register(r'albums', album_views.AlbumViewSet, basename='album')
router.register(r'reviews', album_views.ReviewViewSet)
router.register(r'genders', genders_views.GendersViewSet)
router.register(r'subgenrer', genders_views.SubgenresViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('', include(router.urls)),
   path('api/', include('users.urls')),
   path("countartist/", count_artist, name="count_artist"),
   path('count/', count_view, name='count'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)