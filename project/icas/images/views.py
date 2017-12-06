from images.models import Image
from rest_framework import viewsets
from images.serializers import ImageSerializer

class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.all().order_by('created')


