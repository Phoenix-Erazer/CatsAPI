from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from catalog.views import CatImageViewSet, proxy_cats_api

router = DefaultRouter()
router.register(r"cats", CatImageViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('api/proxy/cats/', proxy_cats_api),
]
