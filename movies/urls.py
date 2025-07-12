from django.urls import path
from movies.views import MovieDetailsViews, MovieViews


urlpatterns = [
    path('movies/', MovieViews.as_view()),
    path('movies/<int:movie_id>', MovieDetailsViews.as_view()),
]
