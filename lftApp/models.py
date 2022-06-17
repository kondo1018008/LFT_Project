from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Player(models.Model):
    player_name = models.CharField(max_length=100)

    def __str__(self):
        return self.player_name

class LFT(models.Model):
    lft_name = models.CharField(max_length=100)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
