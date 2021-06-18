from django.urls import path
from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import UserView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='rest_register'),
    path('user/<int:pk>', UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]