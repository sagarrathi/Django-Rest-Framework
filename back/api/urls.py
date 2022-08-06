#Django
from django.urls import path

#Django Rest
from rest_framework.authtoken.views import obtain_auth_token

# Django Rest Simplejwt
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

#API    
from .import views



urlpatterns= [
    path('auth/', obtain_auth_token),
    path('', views.api_home), # localhost:8000/api/
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
 

]