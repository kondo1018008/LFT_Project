from django.contrib import admin
from .models import LFT, Player, Game, Player_Game


# Register your models here.

admin.site.register(Player)
admin.site.register(LFT)
admin.site.register(Game)
admin.site.register(Player_Game)

