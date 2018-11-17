from rest_framework import serializers

from .models import Word
from .models import Game
from .models import GameDetail


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id', 'name')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'member_count', 'mode')


class GameDetailSerializer(serializers.ModelSerializer):
    game = GameSerializer()

    class Meta:
        model = GameDetail
        fields = '__all__'
