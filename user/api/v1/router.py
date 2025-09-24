# user/api/v1/router.py

from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet, BookViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)


urlpatterns = router.urls