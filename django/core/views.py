from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.urls import reverse

from .models import Movie, Person, Vote
from .forms import VoteForm
# Create your views here.


class MovieList(ListView):
    model = Movie
    context_object_name = "movie_list"
    template_name = "core:MovieList"
    paginate_by = 2


class MovieDetail(DetailView):
    queryset = (
        Movie.objects.all_with_related_persons()
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            vote = Vote.objects.get_vote_or_unsaved_blank_vote(
                movie=self.object,
                user=self.request.user
            )
            if vote.id:
                vote_form_url = reverse(
                    'core:UpdateVote',
                    kwargs={
                        "movie_id": vote.movie.id,
                        "pk": vote.id
                    }
                )
            else:
                vote_form_url = (
                    reverse(
                        "core:CreateVote",
                        kwargs={
                            "movie_id": self.object.id
                        }
                    )
                )

            vote_form = VoteForm(instance=vote)
            context['vote_form'] = vote_form
            context['vote_form_url'] = vote_form_url

        return context


class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()
