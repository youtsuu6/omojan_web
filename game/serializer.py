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
    # game = GameSerializer()
    words = WordSerializer(many=True, read_only=True)

    class Meta:
        model = GameDetail
        fields = (
        'id', 'game', 'member_name', 'turn_count', 'selected_word_id_1', 'selected_word_id_2', 'point', 'created_at',
        'updated_at', 'words')

