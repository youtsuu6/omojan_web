# import django_filters
import json

from rest_framework import viewsets
from rest_framework.views import APIView
# from rest_framework.views import UpdateView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view
from rest_framework import status
from django_filters import rest_framework as filters
from django.db import transaction
from django.forms.models import model_to_dict

from .models import Word
from .models import Game
from .models import GameDetail
from .serializer import WordSerializer
from .serializer import GameSerializer
from .serializer import GameDetailSerializer
from .serializer import NewGameSerializer

import random

import logging
logger = logging.getLogger('game')

# フィルター
class WordFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Word:
        model = Word
        fields = ['name']


class GameFilter(filters.FilterSet):
    member_count = filters.NumberFilter(lookup_expr='exact')
    mode = filters.CharFilter(lookup_expr='exact')

    class Game:
        model = Game
        fields = ['member_count', 'mode']


class GameDetailFilter(filters.FilterSet):
    game = filters.NumberFilter(lookup_expr='exact')
    member_name = filters.CharFilter(lookup_expr='exact')
    turn_count = filters.NumberFilter(lookup_expr='exact')

    class GameDetail:
        model = GameDetail
        fields = ['game', 'member_name', 'turn_count']


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_class = WordFilter


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_class = GameFilter


class GameDetailViewSet(viewsets.ModelViewSet):
    queryset = GameDetail.objects.all()
    serializer_class = GameDetailSerializer
    filter_class = GameDetailFilter


class NewGameAPI(APIView):

    def post(self, request, format=None):

        new_game_serializer = NewGameSerializer(data={
            'mode': request.data['mode'],
            'member_count': request.data['member_count'],
            'member_name': request.data['member_name'],
        })

        if not new_game_serializer.is_valid():
            return Response({'error': 'POST失敗'}, status=status.HTTP_400_BAD_REQUEST)

        insert_data = new_game_serializer.validated_data

        # ゲーム親と詳細の初期状態を作成
        with transaction.atomic():
            game = Game.objects.create(
                mode=insert_data['mode'],
                member_count=insert_data['member_count']
            )

            game_detail = GameDetail.objects.create(
                member_name=insert_data['member_name'],
                turn_count=1,
                game=game
            )

            # 単語6個をランダムで設定
            word_list = list(Word.objects.filter(is_deleted=False).values('id', 'name'))
            selected_word_list = random.sample(word_list, 6)

            for selected_word in selected_word_list:
                Word(id=selected_word['id']).game_detail.add(game_detail.id)

        response_data = {
            'game': model_to_dict(game),
            'game_detail': model_to_dict(game_detail),
            'words': selected_word_list
        }

        return Response(json.dumps(response_data), status=status.HTTP_201_CREATED)
