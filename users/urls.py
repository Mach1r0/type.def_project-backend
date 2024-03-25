from django.urls import path, include
from .views import RegisterUserView, LoginUserView, UserView, LogoutView

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('login/', LoginUserView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
]