from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from catalog.views import CatImageViewSet

router = DefaultRouter()
router.register(r"cats", CatImageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
