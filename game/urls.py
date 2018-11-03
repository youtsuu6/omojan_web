from rest_framework import routers
from .views import WordViewSet


router = routers.DefaultRouter()
router.register(r'words', WordViewSet)
