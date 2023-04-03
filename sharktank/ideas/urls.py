from django.urls import path

from . import views

app_name = 'ideas'
urlpatterns = [
    # ex: /games/
    path('', views.GameIndexView.as_view(), name='index'),
    # ex: /games/5/
    path('<int:pk>/', views.game_detail, name='game_detail'),
    # ex: /games/5/ideas/1/
    path('<int:game_id>/ideas/<int:idea_id>/', views.idea_detail, name='idea_detail'),
]