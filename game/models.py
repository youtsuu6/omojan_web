from django.db import models


class Game(models.Model):
    SINGLE_MODE = 'single'
    MULTI_MODE = 'multi'
    MODE_CHOICES = (
        (SINGLE_MODE, '1人用'),
        (MULTI_MODE, '複数対戦')
    )
    member_count = models.IntegerField()
    mode = models.CharField(
        max_length=255,
        choices=MODE_CHOICES,
        default=SINGLE_MODE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class GameDetail(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    member_name = models.CharField(max_length=255)
    turn_count = models.IntegerField()
    selected_word_id_1 = models.IntegerField(null=True)
    selected_word_id_2 = models.IntegerField(null=True)
    point = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class Word(models.Model):
    name = models.CharField(max_length=255)
    game_detail = models.ManyToManyField(GameDetail, related_name='words')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
