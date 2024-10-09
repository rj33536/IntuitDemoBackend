from django.urls import path
from .views import UserCreateAPIView, UserLoginAPIView, EventUpdateAPIView

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('update-events/', EventUpdateAPIView.as_view(), name='update-events'),
]