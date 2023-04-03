from django.db import models


class Game(models.Model):
    game_date = models.DateTimeField("game date")


class Presenter(models.Model):
    name = models.CharField("presenter name", max_length=200)


class Idea(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    presenter = models.OneToOneField(
        Presenter, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    title = models.CharField(max_length=200)
    submitter_name = models.CharField(max_length=200)
    deck_url = models.URLField()


class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    presenter = models.ForeignKey(Presenter, on_delete=models.DO_NOTHING)
    entertainment_score = models.IntegerField()
    creativity_score = models.IntegerField()
