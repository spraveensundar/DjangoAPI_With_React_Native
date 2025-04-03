from django.urls import path

from .views import SettingView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('settings', SettingView.as_view()),
    path('create-new-setting/', SettingView.as_view())
]

# localhost:8000/api/v1.0/user/test
