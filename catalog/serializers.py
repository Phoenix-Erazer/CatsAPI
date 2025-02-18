from rest_framework import serializers
from catalog.models import CatImage


class CatImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatImage
        fields = "__all__"
