from django.urls import path,include
from User.api.views import RegisterView
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView



urlpatterns = [
    path('user/register/', RegisterView.as_view(), name='register'),
    path('user/login/', TokenObtainPairView.as_view(), name='login'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]