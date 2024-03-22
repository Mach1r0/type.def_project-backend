from django.urls import path 
from user.views import UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('create/', UserView.as_view({
        'post': 'create'
    })),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', UserView.as_view({
        'post': 'login'
    })),
]
