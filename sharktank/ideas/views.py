from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Game, Idea, Presenter, Vote


# Create your views here.
class GameIndexView(generic.ListView):
    template_name = "ideas/index.html"
    context_object_name = "latest_game_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Game.objects.order_by("-game_date")[:5]


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    ideas = Idea.objects.filter(game=game)
    return render(request, "ideas/game_detail.html", {"game": game, "ideas": ideas})


def idea_detail(request, game_id, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    return render(request, "ideas/idea_detail.html", {"idea": idea})
