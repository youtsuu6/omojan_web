# import django_filters
from rest_framework import viewsets, filters

from .models import Word
from .serializer import WordSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
