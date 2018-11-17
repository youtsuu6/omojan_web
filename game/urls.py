from rest_framework import routers
from .views import WordViewSet
from .views import GameViewSet
from .views import GameDetailViewSet

router = routers.DefaultRouter()
router.register(r'words', WordViewSet)
router.register(r'game', GameViewSet)
router.register(r'game_detail', GameDetailViewSet)
