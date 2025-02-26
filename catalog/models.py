from django.db import models


class CatImage(models.Model):
    CATEGORY_CHOICES = [
        ("cute", "Милый"),
        ("funny", "Смешной"),
        ("sleepy", "Сонный"),
        ("playful", "Игривый"),
    ]

    title = models.CharField(max_length=255)
    image_url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="cute"
    )

    def __str__(self):
        return self.title
