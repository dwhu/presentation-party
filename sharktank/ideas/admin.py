from django.contrib import admin

from .models import Game, Idea, Presenter, Vote

# Register your models here.

admin.site.register(Game)
admin.site.register(Presenter)
admin.site.register(Idea)
admin.site.register(Vote)
