# import django_filters
from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import Word
from .serializer import WordSerializer


# フィルター用クラス
class WordFilter(filters.FilterSet):

    # フィルタの定義
    name = filters.CharFilter(lookup_expr='contains')

    class Word:
        model = Word
        fields = ['name']


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_class = WordFilter
