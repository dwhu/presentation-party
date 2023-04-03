from django.urls import path

from . import views

app_name = "ideas"
urlpatterns = [
    # ex: /games/
    path("", views.GameIndexView.as_view(), name="index"),
    # ex: /games/5/
    path("<int:pk>/", views.game_detail, name="game-detail"),
    # ex: /games/5/
    path("<int:pk>/randomize", views.randomize_idea_presenter, name="game-randomize"),
    # ex: /games/5/
    path("<int:pk>/submit", views.idea_submit, name="idea-submit"),
    # ex: /games/5/ideas/1/
    path("<int:game_id>/ideas/<int:idea_id>/", views.idea_detail, name="idea-detail"),
    # ex: /games/5/ideas/1/
    path("<int:game_id>/ideas/<int:idea_id>/vote", views.vote, name="idea-vote"),
    # ex: /games/5/presenters
    path("<int:pk>/presenters", views.presenter_index, name="presenter-index"),
    # ex: /games/5/presenters/1/
    path(
        "<int:game_id>/presenters/<int:pk>",
        views.presenter_detail,
        name="presenter-detail",
    ),
]
