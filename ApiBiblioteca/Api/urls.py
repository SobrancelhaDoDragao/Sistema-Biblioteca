from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.getRoutes),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/VerifyAuthenticated', views.VerifyAuthenticated.as_view()),
    path('api/createuser',views.UserList.as_view()),
    path('api/user/', views.User_Detail.as_view()),
]