from rest_framework import serializers
from catalog.models import CatImage

class CatImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatImage
        fields = ["id", "title", "image", "uploaded_at", "category"]

    def validate_category(self, value):
        valid_categories = ['cute', 'funny', 'sleepy', 'playful']
        if value not in valid_categories:
            raise serializers.ValidationError(f"Invalid category. Choose one from {valid_categories}")
        return value
