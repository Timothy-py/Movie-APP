from django.shortcuts import render
from django.views.generic import ListView, DetailView, GenericViewError


from .models import Movie, Person
# Create your views here.


class MovieList(ListView):
    model = Movie
    context_object_name = "movie_list"
    template_name = "core:MovieList"
    paginate_by = 2


class MovieDetail(DetailView):
    model = Movie
    context_object_name = "movie"


class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()
