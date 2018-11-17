# import django_filters
from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import Word
from .models import Game
from .serializer import WordSerializer
from .serializer import GameSerializer


# フィルター
class WordFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Word:
        model = Word
        fields = ['name']


class GameFilter(filters.FilterSet):
    member_count = filters.NumberFilter(lookup_expr='exact')
    mode = filters.CharFilter(lookup_expr='exact')

    class Word:
        model = Game
        fields = ['member_count', 'mode']


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_class = WordFilter


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_class = GameFilter
