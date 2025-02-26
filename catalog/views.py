from rest_framework import viewsets
from django_filters import rest_framework as filters
from catalog.models import CatImage
from catalog.serializers import CatImageSerializer

class CatImageFilter(filters.FilterSet):
    category = filters.ChoiceFilter(choices=CatImage.CATEGORY_CHOICES)

    class Meta:
        model = CatImage
        fields = ['category']

class CatImageViewSet(viewsets.ModelViewSet):
    queryset = CatImage.objects.all().order_by("-uploaded_at")
    serializer_class = CatImageSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CatImageFilter
