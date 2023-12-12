from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', views.signup.as_view()),
    path('signin/', views.signin.as_view()),
    path('signout/', views.signout.as_view()),
    path('userinfo/', views.userinfo.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('moreinfo/', views.moreinfo.as_view())
]
