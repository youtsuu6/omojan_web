# import django_filters
from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import Word
from .models import Game
from .models import GameDetail
from .serializer import WordSerializer
from .serializer import GameSerializer
from .serializer import GameDetailSerializer


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
