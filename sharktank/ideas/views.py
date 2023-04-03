import random

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
    presenters = Presenter.objects.filter(game=game)
    return render(
        request,
        "ideas/game_detail.html",
        {"game": game, "ideas": ideas, "presenters": presenters},
    )


def presenter_index(request, pk):
    game = get_object_or_404(Game, pk=pk)
    presenters = Presenter.objects.filter(game=game)
    if request.method == "POST":
        presenter = Presenter(game=game, name=request.POST["name"]).save()
        return HttpResponseRedirect(
            reverse("ideas:presenter-detail", args=(game.id, presenter.id))
        )
    else:
        return render(
            request,
            "ideas/presenters_index.html",
            {"game": game, "presenters": presenters},
        )


def presenter_detail(request, game_id, pk):
    presenter = get_object_or_404(Presenter, pk=pk)
    ideas = Idea.objects.filter(game=presenter.game, presenter=presenter)
    return render(
        request, "ideas/presenter_detail.html", {"presenter": presenter, "ideas": ideas}
    )


def idea_submit(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == "POST":
        idea = Idea(
            game=game,
            title=request.POST["title"],
            submitter_name=request.POST["submitter_name"],
            deck_url=request.POST["deck_url"],
        )
        idea.save()
        return HttpResponseRedirect(
            reverse("ideas:idea-detail", args=(game.id, idea.id))
        )
    else:
        return render(request, "ideas/idea_submit.html", {"game": game})


def idea_detail(request, game_id, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    votes = Vote.objects.filter(idea=idea)
    avg_creativity = sum([v.creativity_score for v in votes]) / len(votes)
    avg_entertainment = sum([v.entertainment_score for v in votes]) / len(votes)
    return render(
        request,
        "ideas/idea_detail.html",
        {
            "idea": idea,
            "num_votes": len(votes),
            "avg_creativity": avg_creativity,
            "avg_entertainment": avg_entertainment,
        },
    )


def vote(request, game_id, idea_id):
    idea = get_object_or_404(Idea, pk=idea_id)
    if request.method == "POST":
        Vote(
            idea=idea,
            entertainment_score=request.POST["entertainment_score"],
            creativity_score=request.POST["creativity_score"],
        ).save()
    return HttpResponseRedirect(reverse("ideas:idea-detail", args=(game_id, idea_id)))


def randomize_idea_presenter(request, pk):
    if request.method == "POST":
        game = get_object_or_404(Game, pk=pk)
        ideas = Idea.objects.filter(game=game)
        presenters = Presenter.objects.filter(game=game)
        presenter_count = {p: 0 for p in presenters}
        for idea in ideas:
            idea.presenter = min(presenter_count, key=presenter_count.get)
            presenter_count[idea.presenter] += 1
            idea.save()
    return HttpResponseRedirect(reverse("ideas:game-detail", args=(pk,)))
