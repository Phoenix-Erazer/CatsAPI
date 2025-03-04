from django.db import models
import uuid
import os
from django.utils.text import slugify


def image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)

    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads", "dreams", filename)

class CatImage(models.Model):
    CATEGORY_CHOICES = [
        ("cute", "Милый"),
        ("funny", "Смешной"),
        ("sleepy", "Сонный"),
        ("playful", "Игривый"),
    ]

    title = models.CharField(max_length=255)
    image_url = models.ImageField(
        upload_to=image_file_path, null=True, blank=True,
        default="default.jpg"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="cute"
    )

    def __str__(self):
        return self.title
