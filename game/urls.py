from django.urls import path
from rest_framework import routers
from .views import WordViewSet
from .views import GameViewSet
from .views import GameDetailViewSet
from .views import NewGameAPI


urlpatterns = [
    path('game_new/', NewGameAPI.as_view()),
]

router = routers.DefaultRouter()
router.register(r'words', WordViewSet)
router.register(r'game', GameViewSet)
router.register(r'game_detail', GameDetailViewSet)
