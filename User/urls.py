from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserRegistrationView, UserLoginView, CustomTokenObtainPairView,UserProfileUpdateView,UserPasswordUpdateView
urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
     path('api/profile/', UserProfileUpdateView.as_view(), name='profile-update'),
    path('api/change-password/', UserPasswordUpdateView.as_view(), name='change-password'),
    
]