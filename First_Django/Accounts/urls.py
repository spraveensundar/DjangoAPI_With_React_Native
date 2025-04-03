from django.urls import path

from .views import TestView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('test', TestView.as_view()),
]

# localhost:8000/api/v1.0/user/test
