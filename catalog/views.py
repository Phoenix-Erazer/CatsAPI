from rest_framework import viewsets
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from catalog.models import CatImage
from catalog.serializers import CatImageSerializer


class CatImageViewSet(viewsets.ModelViewSet):
    queryset = CatImage.objects.all().order_by("-uploaded_at")
    serializer_class = CatImageSerializer


@csrf_exempt
def proxy_cats_api(request):
    api_url = 'https://cats-api-hfgi.onrender.com/api/cats/'

    try:
        response = requests.get(api_url)
        return JsonResponse(response.json(), safe=False)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)