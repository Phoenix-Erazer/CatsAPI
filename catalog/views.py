from rest_framework import viewsets
from catalog.models import CatImage
from catalog.serializers import CatImageSerializer


class CatImageViewSet(viewsets.ModelViewSet):
    queryset = CatImage.objects.all().order_by("-uploaded_at")
    serializer_class = CatImageSerializer
