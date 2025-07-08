from django.urls import path
from users.views import UserViews

urlpatterns = [
    path('users/', UserViews.as_view()),
]
