from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from catalog.views import CatImageViewSet

router = DefaultRouter()
router.register(r"cats", CatImageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
