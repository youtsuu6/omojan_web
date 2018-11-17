from rest_framework import routers
from .views import WordViewSet
from .views import GameViewSet

router = routers.DefaultRouter()
router.register(r'words', WordViewSet)
router.register(r'game', GameViewSet)
