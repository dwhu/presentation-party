from django.test import TestCase
from django.urls import reverse

from .models import Game, Idea, Presenter, Vote

# Create your tests here.


class GameIndexTests(TestCase):
    def test_no_games(self):
        """
        If no games exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("ideas:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No games are available.")
        self.assertQuerysetEqual(response.context["latest_game_list"], [])

    def test_game(self):
        """
        Games with a game_date in the past are displayed on the
        index page.
        """
        game = Game.objects.create(game_date="2018-01-01")
        response = self.client.get(reverse("ideas:index"))
        self.assertQuerysetEqual(
            response.context["latest_game_list"],
            [game],
        )


class GameDetailViewTests(TestCase):
    def test_no_ideas(self):
        """
        If no ideas exist, an appropriate message is displayed.
        """
        game = Game.objects.create(game_date="2018-01-01")
        response = self.client.get(reverse("ideas:game-detail", args=(game.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No ideas are available.")
        self.assertQuerysetEqual(response.context["ideas"], [])

    def test_idea(self):
        """
        Ideas with a game_date in the past are displayed on the
        index page.
        """
        game = Game.objects.create(game_date="2018-01-01")
        idea = Idea.objects.create(
            game=game,
            title="test idea",
            submitter_name="dave",
            deck_url="http://google.com",
        )
        response = self.client.get(reverse("ideas:game-detail", args=(game.id,)))
        self.assertContains(response, "Current Ideas")
        self.assertQuerysetEqual(
            response.context["ideas"],
            [idea],
        )


class IdeaDetailViewTests(TestCase):
    def test(self):
        game = Game.objects.create(game_date="2018-01-01")
        idea = Idea.objects.create(
            game=game,
            title="test idea",
            submitter_name="dave",
            deck_url="http://google.com",
        )
        response = self.client.get(
            reverse("ideas:idea-detail", args=(game.id, idea.id))
        )
        self.assertContains(response, "test idea")
        self.assertEqual(
            response.context["idea"],
            idea,
        )
