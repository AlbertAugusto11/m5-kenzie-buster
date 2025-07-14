from django.urls import path
from movies_orders.views import MovieOrderViews


urlpatterns = [
    path('movies/<int:movie_id>/orders/', MovieOrderViews.as_view()),
]
