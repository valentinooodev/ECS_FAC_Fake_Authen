from django.urls import path
from .views import LoginAPIView, AuthenticationAPIView, CheckHealth


app_name = 'api'

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('auth/verify/', AuthenticationAPIView.as_view(), name='auth'),
    path('health', CheckHealth.as_view(), name='check_health'),
]
