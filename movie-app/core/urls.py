from django.urls import path

from .views import MovieList, MovieDetail, CreateVote, UpdateVote, MovieImageUpload, TopMovies, PersonDetail

app_name = 'core'

urlpatterns = [
    path('movies', MovieList.as_view(), name='MovieList'),
    path('movie/<int:pk>', MovieDetail.as_view(), name='MovieDetail'),
    path('movie/<int:movie_id>/vote', CreateVote.as_view(), name='CreateVote'),
    path('movie/<int:movie_id>/vote/<int:pk>', UpdateVote.as_view(), name='UpdateVote'),
    path('movie/<int:movie_id>/image/upload', MovieImageUpload.as_view(), name='MovieImageUpload'),
    path('movies/top', TopMovies.as_view(), name='TopMovies'),
    path('movies/person/<int:pk>', PersonDetail.as_view(), name='PersonDetail'),
]