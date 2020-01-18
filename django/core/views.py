from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from .models import Movie
# Create your views here.


class MovieList(ListView):
    model = Movie
    context_object_name = "movie_list"
    template_name = "core:MovieList"
    paginate_by = 2


class MovieDetail(DetailView):
    model = Movie
    context_object_name = "movie"