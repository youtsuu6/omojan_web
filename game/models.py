from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


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
