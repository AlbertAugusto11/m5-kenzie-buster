from django.urls import path
from users.views import LoginJWTView, UserDetailViews, UserViews
from rest_framework_simplejwt import views

urlpatterns = [
    path('users/', UserViews.as_view()),
    path('users/login/', LoginJWTView.as_view()),
    path('users/login/refresh/', views.TokenRefreshView.as_view()),
    path('users/<int:user_id>/', UserDetailViews.as_view())
]
