from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Game(models.Model):
    game_title = models.CharField(max_length=200)

    class Meta:
        db_table = 'game'
        verbose_name = 'ゲームタイトル'
        verbose_name_plural = 'ゲームタイトル群'

    def __str__(self):
        return self.game_title


class Player(models.Model):
    player_name = models.CharField(max_length=100)
    player_twitter_link = models.URLField(null=True)
    player_discord_link = models.URLField(null=True)

    class Meta:
        db_table = 'player'
        verbose_name = 'プレイヤー'
        verbose_name_plural = 'プレイヤー群'


    def __str__(self):
        return self.player_name


# class Player_Game(models.Model):
#     Player = models.ForeignKey(Player, on_delete=models.CASCADE)
#     Game = models.ForeignKey(Game, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = 'player_game_relation'


class LFT(models.Model):
    lft_name = models.CharField(max_length=100)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        db_table = 'lft'
        verbose_name = 'LFT'
        verbose_name_plural = 'LFT群'


    def __str__(self):
        return self.lft_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
